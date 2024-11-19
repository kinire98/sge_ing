```python
import os
from datetime import datetime
from typing import Callable
from dateutil.parser import parse
_RESET = '\033[0m'
_BLACK = '\033[30m'
_RED = '\033[31m'
_GREEN = '\033[32m'
_YELLOW = '\033[33m' # orange on some systems
_BLUE = '\033[34m'
_MAGENTA = '\033[35m'
_CYAN = '\033[36m'
_LIGHT_GRAY = '\033[37m'
_DARK_GRAY = '\033[90m'
_BRIGHT_RED = '\033[91m'
_BRIGHT_GREEN = '\033[92m'
_BRIGHT_YELLOW = '\033[93m'
_BRIGHT_BLUE = '\033[94m'
_BRIGHT_MAGENTA = '\033[95m'
_BRIGHT_CYAN = '\033[96m'
_WHITE = '\033[97m'

_BACKGROUND_BLACK = '\033[40m'
_BACKGROUND_RED = '\033[41m'
_BACKGROUND_GREEN = '\033[42m'
_BACKGROUND_YELLOW = '\033[43m' # orange on some systems
_BACKGROUND_BLUE = '\033[44m'
_BACKGROUND_MAGENTA = '\033[45m'
_BACKGROUND_CYAN = '\033[46m'
_BACKGROUND_LIGHT_GRAY = '\033[47m'
_BACKGROUND_DARK_GRAY = '\033[100m'
_BACKGROUND_BRIGHT_RED = '\033[101m'
_BACKGROUND_BRIGHT_GREEN = '\033[102m'
_BACKGROUND_BRIGHT_YELLOW = '\033[103m'
_BACKGROUND_BRIGHT_BLUE = '\033[104m'
_BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
_BACKGROUND_BRIGHT_CYAN = '\033[106m'
_BACKGROUND_WHITE = '\033[107m'

_TAB = "\t"
def main_menu() -> int:
    """Menu principal"""
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Añadir tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Eliminar/Archivar tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Marcar tarea como completada", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Desarchivar tareas", _RESET))
    print(txt.format(_WHITE, _BACKGROUND_BLACK, 6,  "Salir", _RESET))
    return _get_option(1, 6, main_menu)
def list_tasks_menu() -> int:
    """
    Menú para listar tareas
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar todas las tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Listar tareas completadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Listar tareas sin completar", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Filtros y orden personalizados", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Tareas archivadas", _RESET))
    print(txt.format(_WHITE, _BACKGROUND_BLACK, 6,  "Salir", _RESET))
    return _get_option(1, 6, list_tasks_menu)

def list_archived_tasks_menu() -> int:
    """
    Menú para las tareas archivadas
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar todas las tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Listar tareas completadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Listar tareas sin completar", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Filtros y orden personalizados", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5, list_archived_tasks_menu)
def custom_filters() -> int:
    """
    Decide si aplicar filtros u orden a los elementos
    Cuando se salga de esta vista se aplicarán los filtros y se mostrarán
    las tareas que apliquen en el orden decidido
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Filtros", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Orden", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3, "Salir y aplicar filtros", _RESET))
    return _get_option(1, 3, custom_filters)
def filters_menu() -> int:
    """
    Opciones del menú de filtros
    Decide el parámetro de filtro
    Se puede aplicar más de un filtro
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Nombre", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Prioridad", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Fecha", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Completadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Limpiar filtros", _RESET))
    print(txt.format(_WHITE, _BACKGROUND_BLACK, 6,  "Salir", _RESET))
    return _get_option(1, 6, filters_menu)
def name_filter_menu() -> str:
    """
    Pregunta al usuario por la expresión regular para el filtrado de tareas por nombre
    """
    _clear_terminal()
    return input("Introduce la expresión regular para los nombres de tareas: ")

def priority_filter_menu() -> list[int]:
    """
    Pregunta al usuario por las prioridades por las que quiere filtrar separadas por comas
    Tienen que ser números enteros entre 1 y 10
    """
    _clear_terminal()
    priorities = input("Introduce las prioridades, entre 1 y 10, que quieres que aparezcan separadas por comas: ").split(",")
    return list(map(
            lambda x: int(x),
            priorities
            )) if _is_valid_int_list(priorities) else priority_filter_menu()
def _is_valid_int_list(values: list[str]) -> bool:
    """
    Comprueba si los indices de la lista son números válidos
    """
    for value in values:
        try:
            int_value = int(value)
            if int_value < 1 or int_value > 10:
                return False
        except ValueError:
            return False
    return True
def date_filter_menu() -> str:
    """
    Pregunta una fecha al usuario para utilizar en los filtros
    En caso de dejar el campo vacío se utilizará la fecha actual
    """
    _clear_terminal()
    date = input("Introduce una fecha con formato [dd/mm/aaaa] (ENTER para fecha actual): ")
    if len(date) == 0:
        return datetime.now().strftime("%d/%m/%Y")
    return date if _check_correct_date(date) else date_filter_menu()
def _check_correct_date(date: str) -> bool:
    """
    Comprobador utilizado para asegurarse que la cadena introducida por el usuario
    representa una fecha correcta coherente con el formato que se guarda en el CSV
    """
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False
def before_after_equal_date() -> int:
    """
    Menú para decidir si el usuario quiere que se muestre antes, después, la misma, antes o la misma, después
    o la misma o una fecha distinta a la introducida
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Antes", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Después", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3, "Igual", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Antes o igual", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Después o igual", _RESET))
    print(txt.format(_WHITE, _BACKGROUND_BLACK, 6,  "Antes o después", _RESET))
    return _get_option(1, 6, before_after_equal_date)
def completed_filter_menu() -> bool:
    """
    Función externa para devolver un bool habiendo decidido si 
    el usuario habiendo introducido un 1 o un 2 la si ha decidido si
    el filtro va a ser para las completadas/no completadas
    """
    return True if _completed_filter_menu() == 1 else False

def _completed_filter_menu() -> int:
    """
    Menú para decidir si el filtro de tareas completadas es para
    las completadas o las no completadas.
    Función interna porque el usuario va a marcar un 1 o 2 y es necesario 
    un bool por tanto esta es una función interna
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Sí", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "No", _RESET))
    return _get_option(1, 2, _completed_filter_menu)


def orders_menu() -> int:
    """
    Menú para que el usuario decida por que parámetro quiere ordenar la lista de tareas
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print("NOTA: Solo se puede ordenar por un parametro a la vez")
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Nombre", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Prioridad", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Fecha", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Limpiar orden", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5, orders_menu)
def ascending_descending() -> int:
    """
    Menú para decidir si el usuario selecciona un orden ascendente o descendente
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Ascendente", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Descendente", _RESET))
    return _get_option(1, 2, ascending_descending)

def delete_archive() -> int:
    """
    Menú para decidir si se elimina o se archiva una tarea
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Eliminar", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Archivar", _RESET))
    return _get_option(1, 2, delete_archive)
def archived_not_archived() -> int:
    """
    Menú para decidir si se elimina una tarea archivada/no archivada
    """
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "No archivadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Archivadas", _RESET))
    return _get_option(1, 2, archived_not_archived)
def print_tasks(tasks: list[dict]):
    """
    Imprimidor externo de las tareas.
    Solo para visualización
    """
    _print_tasks(tasks) 
    print()
    print()
    input("Presiona ENTER para continuar")

def get_task_to_complete(tasks: list[dict]) -> int:
    """
    Devuelve el índice de la lista a archivar/desarchivar/eliminar/marcar como completada
    Este sí es el índice real de la lista.
    En caso de no haber tareas, no se imprime nada y se devuelve un -1
    """
    _clear_terminal()
    if len(tasks) == 0:
        print("No hay tareas")
        input()
        return -1
    return _get_task_to_complete(tasks) - 1
def _get_task_to_complete(tasks: list[dict]) -> int:
    """
    Devuelve el índice de las listas para archivar/desarchivar/eliminar/marcar como completada
    Este no es el índice de la lista, sino uno más para que sea coherente con lo que se le muestra
    al usuario
    """
    _print_tasks(tasks)
    return _get_option_delete_mark_completed(1, len(tasks), _get_task_to_complete, tasks)

def _print_tasks(tasks: list[dict]):
    """
    Imprimidor interno del módulo para las tareas
    """
    counter = 1
    today = datetime.now()
    fmt = "{}{}{:>3}. {}{:<20} {}{:<9} {}{:<15} {}{:<12}{}"
    os.system("cls" if os.name == "nt" else "printf '\033c'")
    print(
            fmt.format(
                _BLACK,
                _BACKGROUND_WHITE,
                "Nº",
                _BACKGROUND_MAGENTA,
                "Nombre",
                _BACKGROUND_RED,
                "Prioridad",
                _BACKGROUND_CYAN,
                "Fecha límite",
                _BACKGROUND_GREEN,
                "¿Completada?",
                _RESET
                )
            )
    for task in tasks:
        date = datetime.strptime(task["limit_date"], "%d/%m/%Y")
        print(
                fmt.format(
                    "",
                    "",
                    counter,
                    "",
                    task["name"],
                    "",
                    task["priority"],
                    (f"{_BLACK}{_BACKGROUND_GREEN}" if date > today else f"{_BLACK}{_BACKGROUND_RED}"),
                    task["limit_date"] + _RESET + "     ",
                    "",
                    (f"{_BLACK}{_BACKGROUND_GREEN}Sí" if task["completed"] == "true" else f"{_BLACK}{_BACKGROUND_RED}No"),
                    _RESET
                    )
                )
        counter += 1

def get_priority() -> int:
    """
    Pregunta al usuario por la prioridad de la tarea, un número entre 1 y 10
    En caso de no se uno de esos valores, seguirá preguntando
    """
    _clear_terminal()
    print("Introduce una prioridad para la tarea")
    return _get_option(1, 10, get_priority)
def get_date() -> str:
    """
    Preguntar al usuario la fecha para la tarea a añadir.
    La fecha tendrá un formato dd/mm/YYYY.
    En caso de no responder nada será la fecha actual.
    En caso de ser una fecha errónea el usuario tendrá que seguir respondiendo hasta que introduzca
    una fecha correcta
    """
    _clear_terminal()
    date = input("Introduce una fecha para añadir con formato [dd/mm/aaaa] (ENTER para fecha actual): ")
    if len(date) == 0:
        return datetime.now().strftime("%d/%m/%Y")
    return date if _check_correct_date(date) else get_date()
def get_task_name() -> str:
    """
    Preguntar al usuario el nombre de la tarea a añadir
    """
    _clear_terminal()
    return input("Introduce un nombre para la nueva tarea: ")
def error_opening_file():
    """
    Salida para informar al usuario de que hubo un error en la carga de los archivos y se finalizará el programa
    sin importar la operación pendiente
    """
    _clear_terminal()
    print("Hubo un error y se finalizará el programa")
    input()








def _get_option(min: int, max: int, f: Callable[[], int]) -> int:
    """
    Preguntar al usuario por una opcion entre el maximo y el minimo.
    Hasta que no se introduzca una opcion correcta, no se dejara de preguntar.
    Se volverá a ejecutar la función que se introduce por parámetro para evitar
    que se acumulen las preguntas por entrada de usuario
    """
    try:
        out = int(input(f"Selecciona una opcion entre {min} y {max}: "))
    except ValueError:
        out = f()
    if out < min or out > max:
        out = f()
    return out
def _get_option_delete_mark_completed(min: int, max: int, f: Callable[[list[dict]], int], tasks: list[dict]) -> int:
    """
    Preguntar al usuario por una opcion entre el maximo y el minimo.
    Hasta que no se introduzca una opcion correcta, no se dejara de preguntar
    Se volverá a ejecutar la función que se introduce por parámetro para evitar
    que se acumulen las preguntas por entrada de usuario
    En este caso se necesita para volver a imprimir las tareas
    """
    try:
        out = int(input(f"Selecciona una opcion entre {min} y {max}: "))
    except ValueError:
        out = f(tasks)
    if out < min or out > max:
        out = f(tasks)
    return out
def _clear_terminal():
    """
    Limpia el terminal.
    Al utilizarse en diversos puntos, se utiliza esta función para que en caso de tener
    que hacer algún cambio solo se tenga que hacer en un sitio
    """
    os.system("cls" if os.name == "nt" else "printf '\033c'")
```
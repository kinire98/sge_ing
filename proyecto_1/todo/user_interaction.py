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
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Eliminar tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Marcar tarea como completada", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5, main_menu)
def list_tasks_menu() -> int:
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
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar todas las tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Listar tareas completadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Listar tareas sin completar", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Filtros y orden personalizados", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5, list_archived_tasks_menu)
def archived_tasks_menu() -> int:
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar todas las tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Listar tareas completadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Listar tareas sin completar", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Filtros y orden personalizados", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5, list_tasks_menu)
def custom_filters() -> int:
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Filtros", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Orden", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3, "Salir y aplicar filtros", _RESET))
    return _get_option(1, 3, custom_filters)
def filters_menu() -> int:
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
    _clear_terminal()
    return input("Introduce la expresión regular para los nombres de tareas: ")

def priority_filter_menu() -> list[int]:
    _clear_terminal()
    priorities = input("Introduce las prioridades, entre 1 y 10, que quieres que aparezcan separadas por comas: ").split(",")
    return list(map(
            lambda x: int(x),
            priorities
            )) if _is_valid_int_list(priorities) else priority_filter_menu()
def _is_valid_int_list(values: list[str]) -> bool:
    for value in values:
        try:
            int_value = int(value)
            if int_value < 1 or int_value > 10:
                return False
        except ValueError:
            return False
    return True
def date_filter_menu() -> str:
    _clear_terminal()
    date = input("Introduce una fecha con formato [dd/mm/aaaa]: ")
    return date if _check_correct_date(date) else date_filter_menu()
def _check_correct_date(date: str) -> bool:
    try:
        parse(date, fuzzy=True)
        return True
    except ValueError:
        return False
def before_after_equal_date() -> int:
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
    return True if _completed_filter_menu() == 1 else False

def _completed_filter_menu() -> int:
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Sí", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "No", _RESET))
    return _get_option(1, 2, _completed_filter_menu)


def orders_menu() -> int:
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
    _clear_terminal()
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Ascendente", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Descendente", _RESET))
    return _get_option(1, 2, ascending_descending)


def print_tasks(tasks: list[dict]):
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
    print()
    print()
    input("Presiona ENTER para continuar")











def _get_option(min: int, max: int, f: Callable[[], int]) -> int:
    """
    Preguntar al usuario por una opcion entre el maximo y el minimo.
    Hasta que no se introduzca una opcion correcta, no se dejara de preguntar
    """
    try:
        out = int(input(f"Selecciona una opcion entre {min} y {max}: "))
    except ValueError:
        out = f()
    if out < min or out > max:
        out = f()
    return out
def _clear_terminal():
    os.system("cls" if os.name == "nt" else "printf '\033c'")

import os
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
    os.system("cls" if os.name == "nt" else "printf '\033c'")
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Añadir tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Eliminar tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Marcar tarea como completada", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5)
def listar_tareas_menu() -> int:
    os.system("cls" if os.name == "nt" else "printf '\033c'")
    txt = "{}{}{:^5}{:<40}{:15}"
    print(txt.format(_BLACK, _BACKGROUND_WHITE, 1,  "Listar todas las tareas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_MAGENTA, 2, "Listar tareas completadas", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_RED, 3,"Listar tareas sin compleatar", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_CYAN, 4, "Filtros y orden personalizados", _RESET))
    print(txt.format(_BLACK, _BACKGROUND_GREEN, 5,  "Salir", _RESET))
    return _get_option(1, 5)
def filtros_personalizados() -> int:
    return 0
def print_tasks(tasks: list[dict]):
    counter = 1
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
        print(
                fmt.format(
                    "",
                    "",
                    counter,
                    "",
                    task["nombre"],
                    "",
                    task["prioridad"],
                    "",
                    task["fecha_limite"],
                    "",
                    (f"{_BLACK}{_BACKGROUND_GREEN}Sí" if task["completada"] == "true" else f"{_BLACK}{_BACKGROUND_RED}No"),
                    _RESET
                    )
                )
        counter += 1
    print()
    print()
    input("Presiona ENTER para continuar")











def _get_option(min: int, max: int) -> int:
    """
    Preguntar al usuario por una opcion entre el maximo y el minimo.
    Hasta que no se introduzca una opcion correcta, no se dejara de preguntar
    """
    try:
        out = int(input(f"Selecciona una opcion entre {min} y {max}: "))
    except ValueError:
        print("Introduce solo numeros")
        out = _get_option(min, max)
    if out < min or out > max:
        print("El numero introducido tiene que estar dentro del rango")
        out = _get_option(min, max)
    return out

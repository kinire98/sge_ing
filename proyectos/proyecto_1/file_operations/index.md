```python
import csv
import os
import sys
from typing import Callable

import user_interaction
def _load_tasks() -> list[dict]:
    """
    Carga las tareas de un archivo CSV y devuelve un array de diccionarios y sus valores
    Si ocurre un error en la carga del archivo se finaliza el programa
    """
    try:
        with open(os.path.dirname(__file__) + "/res/tasks.csv") as csv_file:
            return list(csv.DictReader(csv_file))
    except OSError | IOError | FileNotFoundError:
        user_interaction.error_opening_file()
        sys.exit()
def _load_archived_tasks() -> list[dict]:
    """
    Carga las tareas archivadas de un archivo CSV y devuelve un array de diccionarios y sus valores
    Si ocurre un error en la carga del archivo se finaliza el programa
    """
    try:
        with open(os.path.dirname(__file__) + "/res/archive.csv") as csv_file:
            return list(csv.DictReader(csv_file))
    except OSError | IOError | FileNotFoundError:
        user_interaction.error_opening_file()
        sys.exit()
_tasks = _load_tasks()
_archive = _load_archived_tasks()

def return_tasks(f: Callable[[dict], bool]) -> list[dict]:
    """
    Devuelve las tareas que coincidan con el filtro recibido por parámetro
    """
    return list(filter(
            f,
            _tasks
            ))
def return_archived_tasks(f: Callable[[dict], bool]) -> list[dict]:
    """
    Devuelve las tareas archivadas que coincidan con el filtro recibido por parámetro
    """
    return list(filter(
            f,
            _archive
            ))
def write_files(tasks: list[dict], archived_tasks: list[dict]):
    """
    Recibe las tareas y las tareas archivadas y las guarda en sus respectivos ficheros
    manteniendo las cabeceras del archivo.
    En caso de error al abrir algún archivo el programa finalizará sin importar lo que se haya guardado
    """
    try:
        if len(tasks) != 0:
            with open(os.path.dirname(__file__) + "/res/tasks.csv", "w") as csv_file:
                csv_file.write("name,priority,limit_date,completed\n")
                writer = csv.writer(csv_file, delimiter=",", quotechar='"')
                for task in tasks:
                    writer.writerow(list(task.values()))
        else:
            with open(os.path.dirname(__file__) + "/res/tasks.csv", "w") as csv_file:
                csv_file.write("name,priority,limit_date,completed\n")
        if len(archived_tasks) != 0:
            with open(os.path.dirname(__file__) + "/res/archive.csv", "w") as csv_file:
                csv_file.write("name,priority,limit_date,completed\n")
                writer = csv.writer(csv_file, delimiter=",", quotechar='"')
                for task in archived_tasks:
                    writer.writerow(list(task.values()))
        else: 
            with open(os.path.dirname(__file__) + "/res/archive.csv", "w") as csv_file:
                 csv_file.write("name,priority,limit_date,completed\n")
    except OSError | IOError | FileNotFoundError:
        user_interaction.error_opening_file()
        sys.exit()
```
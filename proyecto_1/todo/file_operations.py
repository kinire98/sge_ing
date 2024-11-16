import csv
import os
from typing import Callable
def load_tasks() -> list[dict]:
    with open(os.path.dirname(__file__) + "/res/tasks.csv") as csv_file:
        return list(csv.DictReader(csv_file))
def load_archived_tasks() -> list[dict]:
    with open(os.path.dirname(__file__) + "/res/archive.csv") as csv_file:
        return list(csv.DictReader(csv_file))
_tasks = load_tasks()
_archive = load_archived_tasks()

def return_tasks(f: Callable[[dict], bool]) -> list[dict]:
    return list(filter(
            f,
            _tasks
            ))
def return_archived_tasks(f: Callable[[dict], bool]) -> list[dict]:
    return list(filter(
            f,
            _archive
            ))
def write_files(tasks: list[dict], archived_tasks: list[dict]):
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



import csv
import os
def load_tasks() -> list[dict]:
    with open(os.path.dirname(__file__) + "/res/tasks.csv") as csv_file:
        return list(csv.DictReader(csv_file))
def load_archived_tasks() -> list[dict]:
    with open(os.path.dirname(__file__) + "/res/archive.csv") as csv_file:
        return list(csv.DictReader(csv_file))
_tasks = load_tasks()
_archive = load_archived_tasks()

def return_tasks(f) -> list[dict]:
    return list(filter(
            f,
            _tasks
            ))
def return_archived_tasks(f) -> list[dict]:
    return list(filter(
            f,
            _archive
            ))
def write_files(tasks: list[dict]):
    with open(os.path.dirname(__file__) + "/res/tasks.csv") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"')
        writer.writerows(tasks)
    with open(os.path.dirname(__file__) + "/res/archive.csv") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"')
        writer.writerows(tasks)


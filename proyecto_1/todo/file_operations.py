import csv
import os
def load_tasks() -> list[dict]:
    with open(os.path.dirname(__file__) + "/res/tasks.csv") as csv_file:
        return list(csv.DictReader(csv_file))
_tasks = load_tasks()

def return_tasks(f) -> list[dict]:
    return list(filter(
            f,
            _tasks
            ))
def write_files(tasks: list[dict]):
    with open(os.path.dirname(__file__) + "/res/tasks.csv") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"')
        writer.writerows(tasks)


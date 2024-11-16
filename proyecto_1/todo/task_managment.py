from os.path import relpath
from typing import Callable
from importlib import reload
import re

from datetime import datetime
import file_operations
from user_interaction import archived_not_archived
def get_all_tasks(archive: bool) -> list[dict]:
    if archive:
        return file_operations.return_archived_tasks(
            lambda _: True
            )
    
    return file_operations.return_tasks(
            lambda _: True
            )
def get_completed_tasks(archive: bool) -> list[dict]:
    if archive:
        return file_operations.return_archived_tasks(
            lambda x: x["completed"] == "true"
            )

    return file_operations.return_tasks(
            lambda x: x["completed"] == "true"
            )
def get_not_completed_tasks(archive: bool) -> list[dict]:
    if archive:
        return file_operations.return_tasks(
            lambda x: x["completed"] == "false"
            )

    return file_operations.return_tasks(
            lambda x: x["completed"] == "false"
            )


def get_tasks_custom_filter(archive: bool, custom_filter: dict) -> list[dict]:
    function_filter = _lambda_filter(custom_filter)
    if archive:
        return _ordered_tasks(file_operations.return_archived_tasks(function_filter), custom_filter)
    return _ordered_tasks(file_operations.return_tasks(function_filter), custom_filter)


def _ordered_tasks(tasks: list[dict], custom_filter: dict) -> list[dict]:
    if custom_filter["orders_present"] == False:
        return tasks
    if custom_filter["order_value"] == "name":
        custom_filter["ascending"] = not custom_filter["ascending"]
    tasks.sort(
            reverse=custom_filter["ascending"],
            key=lambda x: _order_tasks(x, custom_filter)
            )
    return tasks
def _order_tasks(x: dict, custom_filter: dict):
    if custom_filter["order_value"] == "priority":
        return int(x["priority"])
    if custom_filter["order_value"] == "name":
        return x["name"].casefold()
    return x[custom_filter["order_value"]]

def _lambda_filter(custom_filter: dict) -> Callable[[dict], bool]:
    if custom_filter["filters_present"] == False:
        return lambda _: True
    filters = custom_filter["filters"]
    selected = "completed" in filters
    return lambda x: _name_filter(x["name"], filters.get("name", "")) and _completed_filter(x["completed"], filters.get("completed", False), selected) and _priorities_filter(x["priority"], filters.get("priorities", [])) and _dates_filter(x["limit_date"], filters.get("date", dict()).get("date", ""), filters.get("date", dict()).get("option", 0))
def _name_filter(value: str, regex: str) -> bool:
    if len(regex) == 0:
        return True
    return bool(re.match(regex, value))
def _completed_filter(value: str, expected_value: bool, is_selected: bool) -> bool:
    if not is_selected:
        return True
    if value == "false" and expected_value == False:
        return True
    if value == "true" and expected_value == True:
        return True
    return False
def _priorities_filter(value: str, priorities: list[int]) -> bool:
    if len(priorities) == 0:
        return True
    return int(value) in priorities
def _dates_filter(stored_value: str, filter_value: str, option: int) -> bool:
    if option == 0:
        return True
    stored_date = datetime.strptime(stored_value, "%d/%m/%Y")
    filter_date = datetime.strptime(filter_value, "%d/%m/%Y")
    match option:
        case 1:
            return stored_date < filter_date
        case 2:
            return stored_date > filter_date
        case 3:
            return stored_date == filter_date
        case 4:
            return stored_date <= filter_date
        case 5:
            return stored_date >= filter_date
        case _:
            return stored_date != filter_date


def add_task(name: str, priority: int, date: str):
    tasks = file_operations.return_tasks(lambda _: True) 
    archived_tasks = file_operations.return_archived_tasks(lambda _: True)
    tasks.append({
        "name": name,
        "priority": str(priority),
        "limit_date": date,
        "completed": "false"
        })
    file_operations.write_files(tasks, archived_tasks) 
    reload(file_operations) 
def mark_as_completed(idx: int):
    if idx == -1:
        return
    all_tasks = file_operations.return_tasks(lambda _: True) 
    completed_task = get_not_completed_tasks(False)[idx]
    for i in range(len(all_tasks)):
        if completed_task == all_tasks[i]:
            all_tasks[i]["completed"] = "true"
            break
    archived_tasks = file_operations.return_archived_tasks(lambda _: True)
    file_operations.write_files(all_tasks, archived_tasks)
    reload(file_operations)
def unarchive(idx: int):
    if idx == -1:
        return
    tasks = file_operations.return_tasks(lambda _: True) 
    archived_tasks = file_operations.return_archived_tasks(lambda _: True)
    tasks.append(archived_tasks.pop(idx))
    file_operations.write_files(tasks, archived_tasks)
    reload(file_operations)
def archive(idx: int):
    if idx == -1:
        return
    tasks = file_operations.return_tasks(lambda _: True) 
    archived_tasks = file_operations.return_archived_tasks(lambda _: True)
    archived_tasks.append(tasks.pop(idx))
    file_operations.write_files(tasks, archived_tasks)
    reload(file_operations)
def remove(idx: int, archive: bool):
    if idx == -1:
        return
    tasks = file_operations.return_tasks(lambda _: True) 
    archived_tasks = file_operations.return_archived_tasks(lambda _: True)
    if archive:
        archived_tasks.pop(idx)
    else:
        tasks.pop(idx)
    file_operations.write_files(tasks, archived_tasks)
    reload(file_operations)
    

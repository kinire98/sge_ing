from typing import Callable
import file_operations
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
    function_filter = lambda_filter(custom_filter)
    if archive:
        return ordered_tasks(file_operations.return_archived_tasks(function_filter), custom_filter)
    return ordered_tasks(file_operations.return_tasks(function_filter), custom_filter)


def ordered_tasks(tasks: list[dict], custom_filter: dict) -> list[dict]:
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

def lambda_filter(custom_filter: dict) -> Callable[[dict], bool]:
    if custom_filter["filters_present"] == False:
        return lambda _: True

    return lambda _: True

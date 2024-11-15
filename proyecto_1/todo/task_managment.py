import file_operations
def get_all_tasks() -> list[dict]:
    return file_operations.return_tasks(
            lambda _: True
            )


import file_operations
import task_managment
import user_interaction

def main():
    """Punto de entrada a la app"""
    option_selected = user_interaction.main_menu()
    while option_selected != 5:
        match option_selected:
            case 1:
                match user_interaction.list_tasks_menu():
                    case 1:
                        user_interaction.print_tasks(task_managment.get_all_tasks(False))
                    case 2:
                        user_interaction.print_tasks(task_managment.get_completed_tasks(False))
                    case 3:
                        user_interaction.print_tasks(task_managment.get_not_completed_tasks(False))
                    case 4:
                        user_interaction.print_tasks(task_managment.get_tasks_custom_filter(False, custom_filters()))
                    case 5:
                        archived_tasks()
            case 2:
                print("")
            case 3:
                print("")
            case 4:
                print("")
        option_selected = user_interaction.main_menu()

def custom_filters() -> dict:
    filters = {
            "filters_present": False,
            "orders_present": False,
            "filters": {},
            "order_value": "",
            "ascending": False
            }
    option_custom_filters = user_interaction.custom_filters()
    while option_custom_filters != 3:
        match option_custom_filters:
            case 1:
                filters = apply_filters(filters)
            case 2:
                filters = orders(filters)
        option_custom_filters = user_interaction.custom_filters()
    
    return filters
def apply_filters(filters: dict) -> dict:
    return filters

def orders(filters: dict):
    match user_interaction.orders_menu():
        case 1:
            filters["order_value"] = "name"
            filters["ascending"] = True if user_interaction.ascending_descending() == 1 else False
            filters["orders_present"] = True
        case 2:
            filters["order_value"] = "priority"
            filters["ascending"] = True if user_interaction.ascending_descending() == 1 else False
            filters["orders_present"] = True
        case 3:
            filters["order_value"] = "limit_date"
            filters["ascending"] = True if user_interaction.ascending_descending() == 1 else False
            filters["orders_present"] = True
        case 4:
            filters["orders_present"] = False
    return filters


def archived_tasks():
    match user_interaction.list_archived_tasks_menu():
        case 1:
            user_interaction.print_tasks(task_managment.get_all_tasks(True))
        case 2:
            user_interaction.print_tasks(task_managment.get_completed_tasks(True))
        case 3:
            user_interaction.print_tasks(task_managment.get_not_completed_tasks(True))
        case 4:
            user_interaction.print_tasks(task_managment.get_tasks_custom_filter(True, custom_filters()))

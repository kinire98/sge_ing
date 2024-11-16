import file_operations
import task_managment
import user_interaction

def main():
    """Punto de entrada a la app"""
    option_selected = user_interaction.main_menu()
    while option_selected != 6:
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
                task_managment.add_task(user_interaction.get_task_name(), user_interaction.get_priority(), user_interaction.get_date())
            case 3:
                delete_archive()
            case 4:
                task_managment.mark_as_completed(user_interaction.get_task_to_complete(task_managment.get_not_completed_tasks(False)))
            case 5:
                task_managment.unarchive(user_interaction.get_task_to_complete(task_managment.get_all_tasks(True)))
        option_selected = user_interaction.main_menu()

def custom_filters() -> dict:
    """Administador para aplicar los filtros personalizados"""
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
    """
    Guarda los filtros en el diccionario
    """
    match user_interaction.filters_menu():
        case 1:
            filters["filters"]["name"] = user_interaction.name_filter_menu()
            filters["filters_present"] = True
        case 2:
            filters["filters"]["priorities"] = user_interaction.priority_filter_menu()
            filters["filters_present"] = True
        case 3:
            filters["filters"]["date"] = {
                    "date": user_interaction.date_filter_menu(),
                    "option": user_interaction.before_after_equal_date()
                    }
            filters["filters_present"] = True
        case 4:
            filters["filters"]["completed"] = user_interaction.completed_filter_menu()
            filters["filters_present"] = True
        case 5:
            filters["filters_present"] = False
            filters["filters"] = {}

        
    return filters

def orders(filters: dict):
    """
    Guarda la manera de ordenación en el diccionario
    """
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
            filters["order_value"] = ""
            filters["ascending"] = False
    return filters


def archived_tasks():
    """
    Administrador para las tareas archivadas
    """
    match user_interaction.list_archived_tasks_menu():
        case 1:
            user_interaction.print_tasks(task_managment.get_all_tasks(True))
        case 2:
            user_interaction.print_tasks(task_managment.get_completed_tasks(True))
        case 3:
            user_interaction.print_tasks(task_managment.get_not_completed_tasks(True))
        case 4:
            user_interaction.print_tasks(task_managment.get_tasks_custom_filter(True, custom_filters()))
def delete_archive():
    """
    Administrador para borrar/archivar tareas
    """
    match user_interaction.delete_archive():
        case 1:
            match user_interaction.archived_not_archived():
                case 1:
                    task_managment.remove(user_interaction.get_task_to_complete(task_managment.get_all_tasks(False)), False)
                case 2:
                    task_managment.remove(user_interaction.get_task_to_complete(task_managment.get_all_tasks(True)), True)
        case 2:
            task_managment.archive(user_interaction.get_task_to_complete(task_managment.get_all_tasks(False)))

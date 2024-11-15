import file_operations
import task_managment
import user_interaction

def main():
    """Punto de entrada a la app"""
    option_selected = user_interaction.main_menu()
    while option_selected != 5:
        match option_selected:
            case 1:
                listar_option_selected = user_interaction.listar_tareas_menu()
                match listar_option_selected:
                    case 1:
                        user_interaction.print_tasks(task_managment.get_all_tasks())
                    case 2:
                        print()
                    case 3:
                        print()
                    case 4:
                        print()
            case 2:
                print("")
            case 3:
                print("")
            case 4:
                print("")
        option_selected = user_interaction.main_menu()


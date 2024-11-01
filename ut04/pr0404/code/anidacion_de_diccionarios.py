def mostrar_empleados(empleados: dict):
    for key, value in empleados.items():
        print(f"{key}: {value}")
def anadir_empleados(empleados: dict, nombre: str, funcion: str) -> bool:
    if empleados.get(nombre, 0) != 0:
        print(f"{nombre} ya trabaja en este departamento")
        return False
    empleados[nombre] = funcion
    return True
def eliminar_empleados(empleados: dict, nombre: str) -> bool:
    if empleados.get(nombre, 0) == 0:
        print(f"{nombre} no trabaja en este departamento")
        return False
    del empleados[nombre]
    return True
def mostrar_todos_empleados(empleados: dict):
    for key, value in empleados.items():
        print(f"Departamento {key}: ")
        for k, val in value.items():
            print(f"{k}: {val}")
def main(dptos: dict):
    print("Elige una opción: ")
    print("1. Listar empleados de un departamento")
    print("2. Inscribir empleado en un departamento")
    print("3. Echar a un empleado de un departamento")
    opcion = input("Elige lo que quieres hacer [1/2/3]: ")

    while(opcion not in ["1", "2", "3"]):
        print("Elige una opción válida")
        opcion = input("Elige lo que quieres hacer [1/2/3]: ")

    dpto = input("Introduce el nombre de un departamento: ")

    if dptos.get(dpto, 0) == 0:
        print("El departamento no existe")
        return
    match opcion:
            case "1":
                print(dptos[dpto])
                mostrar_empleados(dptos[dpto])
            case "2":
                if anadir_empleados(dptos[dpto], 
                                 input("Introduce el nombre del empleado: "),
                                    input("Introduce la funcion del empleado en el departamento: ")):
                    mostrar_todos_empleados(dptos)
            case "3":
                if eliminar_empleados(dptos[dpto],
                                      input("Introduce el nombre del empleado: ")):
                    mostrar_todos_empleados(dptos)


departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}
main(departamentos)

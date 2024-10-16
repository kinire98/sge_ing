from random import randint
mostrar_opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"] # mostrar
opcion = input("Escoge una de las siguientes opciones " + str(mostrar_opciones) + ": ")
while (not opcion in mostrar_opciones):
    print("Introduce una opcion valida")
    opcion = input("Escoge una de las siguientes opciones " + str(mostrar_opciones) + ": ")
match (opcion, randint(0, 4)):
    case ("Piedra", 0):
        print("Tu eleccion: Piedra")
        print("La eleccion del programa: Piedra")
        print("Empate")
    case ("Papel", 1):
        print("Tu eleccion: Papel")
        print("La eleccion del programa: Papel")
        print("Empate")
    case ("Tijera", 2):
        print("Tu eleccion: Tijera")
        print("La eleccion del programa: Tijera")
        print("Empate")
    case ("Lagarto", 3):
        print("Tu eleccion: Lagarto")
        print("La eleccion del programa: Lagarto")
        print("Empate")
    case ("Spock", 4):
        print("Tu eleccion: Spock")
        print("La eleccion del programa: Spock")
        print("Empate")
    case ("Piedra", 1):
        print("Tu eleccion: Piedra")
        print("La eleccion del programa: Papel")
        print("Pierdes")
    case ("Piedra", 2):
        print("Tu eleccion: Piedra")
        print("La eleccion del programa: Tijera")
        print("Ganas")
    case ("Piedra", 3):
        print("Tu eleccion: Piedra")
        print("La eleccion del programa: Lagarto")
        print("Ganas")
    case ("Piedra", 4):
        print("Tu eleccion: Piedra")
        print("La eleccion del programa: Spock")
        print("Pierdes")
    case ("Papel", 0):
        print("Tu eleccion: Papel")
        print("La eleccion del programa: Piedra")
        print("Ganas")
    case ("Papel", 2):
        print("Tu eleccion: Papel")
        print("La eleccion del programa: Tijeras")
        print("Pierdes")
    case ("Papel", 3):
        print("Tu eleccion: Papel")
        print("La eleccion del programa: Lagarto")
        print("Pierdes")
    case ("Papel", 4):
        print("Tu eleccion: Papel")
        print("La eleccion del programa: Spock")
        print("Ganas")
    case ("Tijeras", 0):
        print("Tu eleccion: Tijeras")
        print("La eleccion del programa: Piedra")
        print("Pierdes")
    case ("Tijeras", 1):
        print("Tu eleccion: Tijeras")
        print("La eleccion del programa: Papel")
        print("Ganas")
    case ("Tijeras", 3):
        print("Tu eleccion: Tijeras")
        print("La eleccion del programa: Lagarto")
        print("Ganas")
    case ("Tijeras", 4):
        print("Tu eleccion: Tijeras")
        print("La eleccion del programa: Spock")
        print("Pierdes")
    case ("Lagarto", 0):
        print("Tu eleccion: Lagarto")
        print("La eleccion del programa: Piedra")
        print("Pierdes")
    case ("Lagarto", 1):
        print("Tu eleccion: Lagarto")
        print("La eleccion del programa: Papel")
        print("Ganas")
    case ("Lagarto", 2):
        print("Tu eleccion: Lagarto")
        print("La eleccion del programa: Tijeras")
        print("Pierdes")
    case ("Lagarto", 4):
        print("Tu eleccion: Lagarto")
        print("La eleccion del programa: Spock")
        print("Ganas")
    case ("Spock", 0):
        print("Tu eleccion: Spock")
        print("La eleccion del programa: Piedra")
        print("Ganas")
    case ("Spock", 1):
        print("Tu eleccion: Spock")
        print("La eleccion del programa: Papel")
        print("Pierdes")
    case ("Spock", 2):
        print("Tu eleccion: Spock")
        print("La eleccion del programa: Tijeras")
        print("Ganas")
    case ("Spock", 3):
        print("Tu eleccion: Spock")
        print("La eleccion del programa: Lagarto")
        print("Pierdes")
    



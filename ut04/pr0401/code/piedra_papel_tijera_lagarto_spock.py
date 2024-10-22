from random import randint
mostrar_opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"] # mostrar
victoria_jugador = 0
victoria_maquina = 0
while (victoria_jugador < 5 and victoria_maquina < 5):
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
            victoria_maquina += 1
        case ("Piedra", 2):
            print("Tu eleccion: Piedra")
            print("La eleccion del programa: Tijera")
            print("Ganas")
            victoria_jugador += 1
        case ("Piedra", 3):
            print("Tu eleccion: Piedra")
            print("La eleccion del programa: Lagarto")
            print("Ganas")
            victoria_jugador += 1
        case ("Piedra", 4):
            print("Tu eleccion: Piedra")
            print("La eleccion del programa: Spock")
            print("Pierdes")
            victoria_maquina += 1
        case ("Papel", 0):
            print("Tu eleccion: Papel")
            print("La eleccion del programa: Piedra")
            print("Ganas")
            victoria_jugador += 1
        case ("Papel", 2):
            print("Tu eleccion: Papel")
            print("La eleccion del programa: Tijeras")
            print("Pierdes")
            victoria_maquina += 1
        case ("Papel", 3):
            print("Tu eleccion: Papel")
            print("La eleccion del programa: Lagarto")
            print("Pierdes")
            victoria_maquina += 1
        case ("Papel", 4):
            print("Tu eleccion: Papel")
            print("La eleccion del programa: Spock")
            print("Ganas")
            victoria_jugador += 1
        case ("Tijeras", 0):
            print("Tu eleccion: Tijeras")
            print("La eleccion del programa: Piedra")
            print("Pierdes")
            victoria_maquina += 1
        case ("Tijeras", 1):
            print("Tu eleccion: Tijeras")
            print("La eleccion del programa: Papel")
            print("Ganas")
            victoria_jugador += 1
        case ("Tijeras", 3):
            print("Tu eleccion: Tijeras")
            print("La eleccion del programa: Lagarto")
            print("Ganas")
            victoria_jugador += 1
        case ("Tijeras", 4):
            print("Tu eleccion: Tijeras")
            print("La eleccion del programa: Spock")
            print("Pierdes")
            victoria_maquina += 1
        case ("Lagarto", 0):
            print("Tu eleccion: Lagarto")
            print("La eleccion del programa: Piedra")
            print("Pierdes")
            victoria_maquina += 1
        case ("Lagarto", 1):
            print("Tu eleccion: Lagarto")
            print("La eleccion del programa: Papel")
            print("Ganas")
            victoria_jugador += 1
        case ("Lagarto", 2):
            print("Tu eleccion: Lagarto")
            print("La eleccion del programa: Tijeras")
            print("Pierdes")
            victoria_maquina += 1
        case ("Lagarto", 4):
            print("Tu eleccion: Lagarto")
            print("La eleccion del programa: Spock")
            print("Ganas")
            victoria_jugador += 1
        case ("Spock", 0):
            print("Tu eleccion: Spock")
            print("La eleccion del programa: Piedra")
            print("Ganas")
            victoria_jugador += 1
        case ("Spock", 1):
            print("Tu eleccion: Spock")
            print("La eleccion del programa: Papel")
            print("Pierdes")
            victoria_maquina += 1
        case ("Spock", 2):
            print("Tu eleccion: Spock")
            print("La eleccion del programa: Tijeras")
            print("Ganas")
            victoria_jugador += 1
        case ("Spock", 3):
            print("Tu eleccion: Spock")
            print("La eleccion del programa: Lagarto")
            print("Pierdes")
            victoria_maquina += 1
    print("Jugador " + str(victoria_jugador) + " - " + str(victoria_maquina) + " Maquina")
    



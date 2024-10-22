# Ejercicios Python
## Ejercicio 1
```python
num = input("Introduce un numero: ")

while(not num.isdigit()):
    print("Error")
    num = input("Introduce un numero: ")
```
## Ejercicio 2
```python
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

for i in range(0, b):
    print(str(a) + " * " + str(i) + " = " + str(a * i))
```
## Ejercicio 3
```python
numero_pisos = int(input("Introduce el numero de pisos: "))
for i in range(0, numero_pisos):
    print("*" + ("*" * i))
```
## Ejercicio 4
```python
niveles = int(input("Introduce el numero de asteriscos que quieres que tenga el ultimo nivel: "))
while (niveles & 1 == 0):
    print("El numero tiene que ser impar")
    niveles = int(input("Introduce el numero de asteriscos que quieres que tenga el ultimo nivel: "))
piramide = ""
for i in range(niveles, 0, -2):
    piramide += (" " * int((niveles - i) / 2)) + ("*" * i) + (" " * int((niveles - i) / 2)) + "\n"
print(piramide[::-1])

```
## Ejercicio 5
```python
import math
numeros = []
for i in range(0,5):
    numeros.append(int(input("Introduce un numero (" + str(5 - i) + " restantes): "))
)
mayor = -math.inf
menor = math.inf

for i in numeros:
    if (i > mayor):
        mayor = i
    if (i < menor):
        menor = i
print("Numero mas grande introducido: " + str(mayor))
print("Numero mas pequeño introducido: " + str(menor))

```
## Ejercicio 6
```python
valores_validos = ["mm", "cm", "dm", "m", "dam", "hm", "km"]4


cantidad = int(input("Introduce una cantidad para convertir: "))

unidad_origen = input("Introduce la unidad a convertir "+ str(valores_validos) + ": ")
while (not unidad_origen in valores_validos):
    print("Introduce un valor valido")
    unidad_origen = input("Introduce la unidad a convertir "+ str(valores_validos) + ": ")

unidad_destino = input("Introduce la unidad a la cual quieres convertir "+ str(valores_validos) + ": ")
while (not unidad_destino in valores_validos):
    print("Introduce un valor valido")
    unidad_destino = input("Introduce la unidad a la cual quieres convertir "+ str(valores_validos) + ": ")

numero_ceros = valores_validos.index(unidad_origen) - valores_validos.index(unidad_destino)
print("Valor anterior: " + str(cantidad) + unidad_origen)
print("Valor convertido: " + str(cantidad * (10 ** numero_ceros)) + unidad_destino)
```
## Ejercicio 7
```python
from random import randint
numero_a_adivinar = randint(0, 101)
adivinado = int(input("Adivina el numero: "))
while (not adivinado==numero_a_adivinar):
    if(adivinado > numero_a_adivinar):
        print("El numero que has introducido es mayor que el que tienes que adivinar")
    elif (adivinado < numero_a_adivinar):
        print("El numero que has introducido es menor que el que tienes que adivinar")
    adivinado = int(input("Adivina el numero: "))
print("Adivinaste el numero")
```
## Ejercicio 8
```python
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
    

 
```
## Ejercicio 9
```python
n =  int(input("Introduce el numero para la secuencia de fibonacci: "))

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

print(a)
```

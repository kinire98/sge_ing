#!/usr/bin/python3
niveles = int(input("Introduce el numero de asteriscos que quieres que tenga el ultimo nivel: "))
while (niveles & 1 == 0):
    print("El numero tiene que ser impar")
    niveles = int(input("Introduce el numero de asteriscos que quieres que tenga el ultimo nivel: "))
piramide = ""
for i in range(niveles, 0, -2):
    piramide += (" " * int((niveles - i) / 2)) + ("*" * i) + (" " * int((niveles - i) / 2)) + "\n"
print(piramide[::-1])

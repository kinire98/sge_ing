#!/usr/bin/python3
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

for i in range(0, b):
    print(str(a) + " * " + str(i) + " = " + str(a * i))

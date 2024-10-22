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


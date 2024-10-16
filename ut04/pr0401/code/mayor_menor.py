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

import random
numeros = []
for i in range(100):
    numeros.append(random.randint(0, 150))
nueva_lista = numeros[::-1]
numeros[0] = numeros[0] * 2
print(numeros)
print(nueva_lista)

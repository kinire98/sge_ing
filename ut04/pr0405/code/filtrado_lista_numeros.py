import random
numeros = []
for i in range(5000):
    numeros.append(random.randint(0, 10000))
lista_ordenada = list(filter(lambda x: x & 1 == 0, numeros))
lista_ordenada.sort()
print(lista_ordenada)

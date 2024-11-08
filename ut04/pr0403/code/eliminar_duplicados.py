import random
numeros = []
for i in range(100_000):
    numeros.append(random.randint(0, 150))
numeros_sin_duplicados = []
numeros_ya_introducidos = dict()
for i in numeros:
    num = numeros_ya_introducidos.get(i, 0)
    if num == 0:
        numeros_sin_duplicados.append(i)
        numeros_ya_introducidos[i] = 1
numeros_sin_duplicados.sort()
print(numeros_sin_duplicados)
print(len(numeros_sin_duplicados))


# Mejor solucion
print(list(set(numeros)))

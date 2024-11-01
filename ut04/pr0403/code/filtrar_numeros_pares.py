import random
numeros = []
for i in range(100_000):
    numeros.append(random.randint(0, 150))
print([
    i for i in numeros if i & 1 == 0
    ])

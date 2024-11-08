import random
numeros1 = []
for i in range(10):
    numeros1.append(random.randint(-10, 10))
numeros2 = []
for i in range(10):
    numeros2.append(random.randint(-10, 10))
interseccion = list(filter(
            lambda x: x in numeros2,
            numeros1
        ))
numeros1.sort()
numeros2.sort()
interseccion.sort()
print(numeros1)
print(numeros2)
print(interseccion)

from functools import reduce
import random
numeros = []
for i in range(5):
    numeros.append(random.randint(1, 10))
print(numeros)
print(
            reduce(
                lambda acc, value: acc * value,
                filter(
                    lambda x: x & 1 == 0,
                    numeros
                ),
                1
            )
        )

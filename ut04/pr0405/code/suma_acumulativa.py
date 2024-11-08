from functools import reduce
import random
numeros = []
for i in range(500):
    numeros.append(random.randint(0, 10000))
print(
        reduce(
                lambda acc, val: acc + val,
                numeros,
                0
            )
        )

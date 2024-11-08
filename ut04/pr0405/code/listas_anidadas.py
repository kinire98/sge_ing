from functools import reduce
import random
numeros = []
for i in range(3):
    tmp = []
    for i in range(3):
        tmp.append(random.randint(-10, 10))
    numeros.append(tmp)
print(numeros)
print(
        reduce(
        lambda acc1, value1: acc1 + value1,
        map(
            lambda x: reduce(
                lambda acc, value: acc + value,
                filter(
                    lambda val: val >= 0,
                    x
                    ),
                0
                ),
            numeros
        ),
        0
    )
)

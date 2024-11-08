from functools import reduce


file = open("./palabras.txt")
palabras = file.read().split()
file.close()
def add(acc, value):
    acc[value] = acc.get(value, 0) + 1
    return acc
print(
        reduce(
            add,
            map(
                lambda x: x.lower(),
                palabras
                ),
            dict()
            )
        )

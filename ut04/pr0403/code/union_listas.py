import random
numeros = []
numeros2 = []
for i in range(100):
    numeros.append(random.randint(0, 150))
    numeros2.append(random.randint(0, 150))
def union_listas(list1: list, list2: list) -> list:
    elements = dict()
    union = []
    for i in list1:
        elements[i] = 1
    for i in list2:
        if elements.get(i, 0) == 1:
            union.append(i);
    return union
print(union_listas(numeros, numeros2))

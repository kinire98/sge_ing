from functools import reduce


lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']

def reduce_list(acc, value):
    acc.append(value)
    return acc

print(
        reduce(
            reduce_list,
            lista2,
            reduce(
                reduce_list,
                lista1,
                []
                )
            )
        )

from functools import reduce
lista1 = [1, 2]
lista2 = [3, 4]
def reduce_list(acc, value):
    acc.append(value)
    return acc
print(
        reduce(
            reduce_list,
            map(
                lambda x: (2, x),
                lista2
                ),
            reduce(
                reduce_list,
                map(
                    lambda x: (1, x),
                    lista1
                    ),
                []
                )
            )
        )

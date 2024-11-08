from functools import reduce


funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]
print(
        list(map(
            lambda x: reduce(
                lambda acc, val: val(acc),
                funciones,
                x
                ),
            numeros
            ))
        )

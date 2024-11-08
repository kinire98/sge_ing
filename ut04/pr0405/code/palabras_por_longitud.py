from functools import reduce
file = open("./palabras.txt")
palabras = file.read().split()
file.close()
def red(acc, value):
    tmp_list = acc.get(len(value), [])
    tmp_list.append(value)
    acc[len(value)] = tmp_list
    return acc
print(
        reduce(
            red,
            palabras,
            dict()
            )
        )

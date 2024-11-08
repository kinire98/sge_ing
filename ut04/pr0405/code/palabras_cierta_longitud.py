file = open("./palabras.txt")
palabras = file.read().split()
file.close()
print(
        list(
            map(
            lambda string: string.upper(),
            filter(
                lambda string: len(string) > 5,
                palabras
                )
            ))
        )

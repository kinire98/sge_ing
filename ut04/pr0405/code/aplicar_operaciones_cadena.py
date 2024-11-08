palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]

print(
        list(map(
            lambda x: x[:1].lower() + x[1:].upper(),
            filter(
                lambda y: len(y) > 3 and y.isupper(),
                palabras
                )
            ))
        )

alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]

print(
        list(map(
            lambda x: x[0],
            filter(
                lambda y: y[1] >= 5,
                alumnos
                )
            ))
        )

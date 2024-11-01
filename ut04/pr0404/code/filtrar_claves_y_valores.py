def filtar_por_salario(salarios: dict[str, float], umbral: float) -> dict:
    filtrado = dict()
    for key, value in salarios.items():
        if value >= umbral:
            filtrado[key] = value
    return filtrado

print(filtar_por_salario({
    "Juan": 1660,
    "Currito": 1100,
    "Jefaso": 2213412
    }, 1500))

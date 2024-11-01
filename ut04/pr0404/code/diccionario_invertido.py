def invert_dictionary(dict_to_invert: dict) -> dict:
    inverted = dict()
    for key, value in dict_to_invert.items():
        inverted[value] = key
    return inverted
asignaturas = {
    "Matemáticas": "Ana",
    "Física": "Elena",
    "Programación": "Carlos",
    "Historia": "María",
    "Inglés": "Sofía",
}
print(invert_dictionary(asignaturas)) # No se pueden introducir valores que no se puedan hashear -> listas, sets o diccionarios

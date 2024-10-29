def frecuencia_caracteres(string: str) -> dict:
    dictionary = {}
    for c in string:
        dictionary[c] = dictionary.get(c, 0) + 1
    return dictionary
print(frecuencia_caracteres(input("Introduce una cadena para saber la frecuencia de caracteres: ")))

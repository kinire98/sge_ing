cadena = input("Introduce la cadena para quitar caracteres repetidos: ")
cadena_sin_repetidos = ""
for c in cadena:
    if (c not in cadena_sin_repetidos):
        cadena_sin_repetidos += c
print(cadena_sin_repetidos)

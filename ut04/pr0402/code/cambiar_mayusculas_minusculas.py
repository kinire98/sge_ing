cadena = input("Introduce la cadena: ")

minus = "abcdefghijklmnñopqrstuvwxyz"

cadena_result = ""
for i in cadena:
    if not i.isalpha():
        cadena_result += i
        continue
    if i in minus:
        cadena_result += i.upper()
        continue
    cadena_result += i.lower()

print(cadena_result)

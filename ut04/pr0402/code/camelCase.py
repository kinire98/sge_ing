string = input("Introduce la cadena: ")
camelCase = ""
upper = False
for i in string:
    if i == " " or i == "-":
        upper = True
        continue
    if upper and camelCase != "":
        upper = False
        camelCase += i.upper()
        continue
    camelCase += i.lower()
print(camelCase)

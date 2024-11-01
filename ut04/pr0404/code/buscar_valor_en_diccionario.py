dicti = {
        "Fresa": 5,
        "Pera": 7,
        "Manzana": 3,
}
fruta = input("Introduce el nombre de una fruta: ")
res = ""
if dicti.get(fruta, 0) != 0:
    res = f"El precio de la fruta es: {dicti.get(fruta, 0)}"
else:
    res = "La fruta no existe"
print(res)

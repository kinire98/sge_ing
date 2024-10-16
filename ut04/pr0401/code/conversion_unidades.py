valores_validos = ["mm", "cm", "dm", "m", "dam", "hm", "km"]
cantidad = int(input("Introduce una cantidad para convertir: "))
unidad_origen = input("Introduce la unidad a convertir "+ str(valores_validos) + ": ")
while (not unidad_origen in valores_validos): unidad_origen = input("Introduce la unidad a convertir "+ str(valores_validos) + ": ")
unidad_destino = input("Introduce la unidad a la cual quieres convertir "+ str(valores_validos) + ": ")
while (not unidad_destino in valores_validos): unidad_destino = input("Introduce la unidad a la cual quieres convertir "+ str(valores_validos) + ": ")
print("Valor anterior: " + str(cantidad) + unidad_origen + "\nValor convertido: " + str(cantidad * (10 ** (valores_validos.index(unidad_origen) - valores_validos.index(unidad_destino)))) + unidad_destino)

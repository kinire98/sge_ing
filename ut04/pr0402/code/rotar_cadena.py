string = input("Introduce la cadena a rotar: ")
num_rot = int(input("Introduce el numero de veces a rotar la cadena: "))
num_rot = num_rot % len(string) # modulo para cuando se introduzca un numero mas grande que la cadena solo quede el numero de rotaciones reales
print(string[num_rot:] + string[:num_rot])

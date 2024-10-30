palabra = input("Introduce una palabra: ")

palabras = open("./palabras.txt").readline().split(" ")[:-1]

print(len([i for i in palabras if i == palabra]))

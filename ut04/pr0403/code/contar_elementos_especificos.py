palabra = input("Introduce una palabra: ")
file = open("./palabras.txt", "r")
palabras = file.readline().split(" ")[:-1]
file.close()
print(len([i for i in palabras if i == palabra]))

import re
file = open("./otono.txt")
file_content = re.split("\n|\\s|\\.|,|:|;", file.read())
file.close()
frecuencia_palabras = dict()
for word in file_content:
    if word == '':
        continue
    frecuencia_palabras[word] = frecuencia_palabras.get(word, 0) + 1
print(frecuencia_palabras.items())

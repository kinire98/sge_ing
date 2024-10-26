string = input("Introduce una serie de palabras: ")
max_length = 0
for i in string.split():
    max_length = max(max_length, len(i))
print(max_length)

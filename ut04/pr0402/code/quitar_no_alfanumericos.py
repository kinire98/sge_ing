string = input("Introduce la cadena: ")
result_string = ""
for i in string:
    if i.isalnum():
        result_string += i
print(result_string)

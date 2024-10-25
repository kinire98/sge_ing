string = input("Introduce la cadena codificada con rle: ")
result = ""
cur_let = ""
app = ""
for i in string:
    if cur_let == "":
        cur_let = i
        continue
    if i.isdigit():
        app += i
        continue
    result += cur_let * int(app)
    cur_let = i
    app = ""
result += cur_let * int(app)
print(result)



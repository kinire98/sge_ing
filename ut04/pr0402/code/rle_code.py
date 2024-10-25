string = input("Introduce la cadena: ")
result = ""
cur_let = ''
app = 0
for i in string:
    if app == 0:
        cur_let = i
        app = 1
        continue
    if i != cur_let:
        result += cur_let + str(app)
        cur_let = i
        app = 1
        continue
    app += 1
result += cur_let + str(app)
print(result)

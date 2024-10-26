cadena_nums = input("Introduce un numero: ")
result = ""
counter = 0
for i in range(len(cadena_nums) - 1, -1, -1):
    result = cadena_nums[i] + result
    counter += 1
    if counter == 3:
        result = "." + result
        counter = 0
print(result)

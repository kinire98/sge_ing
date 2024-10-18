n =  int(input("Introduce el numero para la secuencia de fibonacci: "))

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

print(a)

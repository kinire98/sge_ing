import random
numeros = []
for i in range(100_000):
    numeros.append(random.randint(0, 200_000_000))
print(f"Max: {max(numeros)}")
print(f"Min: {min(numeros)}")

import random
numeros = []
for i in range(100):
    numeros.append(random.randint(0, 150))
media = sum(numeros) / len(numeros)
debajo_media = []
encima_media = []
for i in numeros:
    if i <= media:
        debajo_media.append(i)
        continue
    encima_media.append(i)
debajo_media.sort()
encima_media.sort()
print(f"Media: {media}")
print(f"Por debajo de la media: {debajo_media}")
print(f"Por encima de la media: {encima_media}")

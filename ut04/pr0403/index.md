# Ejercicios listas

	Nota: Del ejercicio 1 al 8 se utilizará la misma lista de cadenas.  
	Por lo tanto no se incluirá en los ejemplos, por brevedad.  
	La dejo debajo:  


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]
```

## Ejercicio 1
### Ordenando elementos
```python
nombres = []
nombres.sort()
print(nombres[::-1])
```
## Ejercicio 2
### Contando elementos
```python
nombres = []
nombres_por_a = [ i for i in nombres if i[0].lower() == "a"]
print(len(nombres_por_a))
```
## Ejercicio 3
### Buscar elementos
```python
nombres = []
nombre_usuario = input("Introduce tu nombre: ")
if nombre_usuario not in nombres:
    print("Tu nombre no está en la lista")
else:
    print(f"Tu nombre está en la posición {nombres.index(nombre_usuario)} de la lista")
```
## Ejercicio 4
### Primeros elementos
```python
nombres = []
nombre_usuario = input("Introduce tu nombres: ")
if nombre_usuario not in nombres:
    print("Tu nombre no esta en la lista")
else:
    print("Delante de ti:\n" + ", ".join(nombres[:nombres.index(nombre_usuario)]))
```
## Ejercicio 5
### Obtener número de nombres de una longitud
```python
nombres = []
longitud_nombres = int(input("Introduce un número: "))
print(f"La cantidad de nombres de longitud {longitud_nombres} es: {len([i for i in nombres if len(i) == longitud_nombres])}")
```
## Ejercicio 6
### Nombres cortos
```python
nombres = []
print(", ".join([i for i in nombres if len(i) <= 4]))
```
## Ejercicio 7
### Número de vocales
```python
nombres = []
vocales_encontradas = dict()
vocales = "aeiou"
for i in nombres:
    for c in i:
        if c in vocales:
            vocales_encontradas[c] = vocales_encontradas.get(c, 0) + 1
print(vocales_encontradas)
```
## Ejercicio 8
### Número de letras
```python
nombres = []
letras = dict()
letras_con_tilde = "áéíóú" 
letras_sin_tilde = "aeiou"
for i in nombres:
    for c in i:
        if c.lower() in letras_con_tilde:
            c = letras_sin_tilde[letras_con_tilde.index(c.lower())]
        letras[c.lower()] = letras.get(c.lower(), 0) + 1
print(letras)
```
## Ejercicio 9
### Sumar elementos de una lista
```python
numeros = [123412, 14234123, 51235, 151515, 2341234, 12341234, 457867, 7456745, 457457456, 265434]
print(f"Suma elementos: {sum(numeros)}")
```
## Ejercicio 10
### Contar elementos específicos
```python
palabra = input("Introduce una palabra: ")
file = open("./palabras.txt", "r")
palabras = file.readline().split(" ")[:-1] # Se cargan las palabras de un archivo y se quita la ultima por contener un salto de linea
file.close()
print(len([i for i in palabras if i == palabra]))
```
## Ejercicio 11
### Eliminar duplicados de lista
```python
import random
numeros = []
for i in range(100_000):
    numeros.append(random.randint(0, 150))
numeros_sin_duplicados = []
numeros_ya_introducidos = dict()
for i in numeros:
    num = numeros_ya_introducidos.get(i, 0)
    if num == 0:
        numeros_sin_duplicados.append(i)
        numeros_ya_introducidos[i] = 1
numeros_sin_duplicados.sort()
print(numeros_sin_duplicados)
print(len(numeros_sin_duplicados)) #151 -> de 0 a 150 hay 151 elementos distintos

# Mejor solucion
print(list(set(numeros)))

```
## Ejercicio 12
### Máximo y mínimo
```python
import random
numeros = []
for i in range(100_000):
    numeros.append(random.randint(0, 200_000_000))
print(f"Max: {max(numeros)}")
print(f"Min: {min(numeros)}")
```
## Ejercicio 13
### Filtrar números pares
```python
import random
numeros = []
for i in range(100_000):
    numeros.append(random.randint(0, 150))
print([
    i for i in numeros if i & 1 == 0
    ])
```
## Ejercicio 14
## Revertir una lista sin `.reverse()`
```python
import random
numeros = []
for i in range(100):
    numeros.append(random.randint(0, 150))
nueva_lista = numeros[::-1]
numeros[0] = numeros[0] * 2
print(numeros) # La primera posición estará duplicada
print(nueva_lista) # La primera posición NO estará duplicada
```
## Ejercicio 15
### Concatenar listas
```python
def concat_lists(list1: list, list2: list) -> list:
    list3 = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            list3.append(list1[i])
        if i < len(list2):
            list3.append(list2[i])
    return list3
print(concat_lists([1, 2, 3], [3, 2, 1]))
```
## Ejercicio 16
### Devolver unión listas
```python
import random
numeros = []
numeros2 = []
for i in range(100):
    numeros.append(random.randint(0, 150))
    numeros2.append(random.randint(0, 150))
def union_listas(list1: list, list2: list) -> list:
    elements = dict()
    union = []
    for i in list1:
        elements[i] = 1
    for i in list2:
        if elements.get(i, 0) == 1:
            union.append(i);
    return union
print(union_listas(numeros, numeros2))
```
## Ejercicio 17
### Dividir una lista
```python
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
```

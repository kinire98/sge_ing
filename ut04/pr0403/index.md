# Ejercicios listas

	Nota: Del ejercicio 1 al 8 se utilizará la misma lista de cadenas. Por lo tanto no se incluirá en los ejemplos, por brevedad. La dejo debajo:
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
palabras = open("./palabras.txt").readline().split(" ")[:-1] # Se cargan las palabras de un archivo y se quita la ultima por contener un salto de linea
print(len([i for i in palabras if i == palabra]))
```
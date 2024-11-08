## Ejercicio 1
### Filtrado de una lista de números
```python
import random
numeros = []
for i in range(5000):
    numeros.append(random.randint(0, 10000))
lista_ordenada = list(filter(lambda x: x & 1 == 0, numeros))
lista_ordenada.sort()
print(lista_ordenada)
```
## Ejercicio 2
### Mapeo de temperaturas
```python
import random
temp_cel = []
for i in range(50):
    temp_cel.append(random.randint(-20, 50))
temp_far = list(
        map(
            lambda x: round(x * (9/5) + 32, 3),
            temp_cel
            )
        )
print(temp_cel)
print(temp_far)
```
## Ejercicio 3
### Suma acumulativa
```python
from functools import reduce
import random
numeros = []
for i in range(500):
    numeros.append(random.randint(0, 10000))
print(
        reduce(
                lambda acc, val: acc + val,
                numeros,
                0
            )
        )
```
## Ejercicio 4
### Palabras con cierta longitud
```python
file = open("./palabras.txt") # archivo de ejemplo
palabras = file.read().split()
file.close()
print(
        list(
            map(
            lambda string: string.upper(),
            filter(
                lambda string: len(string) > 5,
                palabras
                )
            ))
        )
```
## Ejercicio 5
### Multiplicación de números pares
```python
from functools import reduce
import random
numeros = []
for i in range(5):
    numeros.append(random.randint(1, 10))
print(numeros)
print(
            reduce(
                lambda acc, value: acc * value,
                filter(
                    lambda x: x & 1 == 0,
                    numeros
                ),
                1
            )
        )
```
## Ejercicio 6
### Combinar operaciones en listas anidadas
```python
from functools import reduce
import random
numeros = []
for i in range(3):
    tmp = []
    for i in range(3):
        tmp.append(random.randint(-10, 10))
    numeros.append(tmp)
print(numeros)
print(
        reduce(
        lambda acc1, value1: acc1 + value1,
        map(
            lambda x: reduce(
                lambda acc, value: acc + value,
                filter(
                    lambda val: val >= 0,
                    x
                    ),
                0
                ),
            numeros
        ),
        0
    )
)
```
## Ejercicio 7
### Frecuencia de palabras
```python
from functools import reduce
file = open("./palabras.txt") # Archivo de ejemplo
palabras = file.read().split()
file.close()
def add(acc, value):
    acc[value] = acc.get(value, 0) + 1
    return acc
print(
        reduce(
            add,
            map(
                lambda x: x.lower(),
                palabras
                ),
            dict()
            )
        )
```
## Ejercicio 8
### Intersección de conjuntos
```python
import random
numeros1 = []
for i in range(10):
    numeros1.append(random.randint(-10, 10))
numeros2 = []
for i in range(10):
    numeros2.append(random.randint(-10, 10))
interseccion = list(filter(
            lambda x: x in numeros2,
            numeros1
        ))
numeros1.sort()
numeros2.sort()
interseccion.sort()
print(numeros1)
print(numeros2)
print(interseccion)
```
## Ejercicio 9
### Agrupación de palabras por longitud
```python
from functools import reduce
file = open("./palabras.txt")
palabras = file.read().split()
file.close()
def red(acc, value):
    tmp_list = acc.get(len(value), [])
    tmp_list.append(value)
    acc[len(value)] = tmp_list
    return acc
print(
        reduce(
            red,
            palabras,
            dict()
            )
        )
```
## Ejercicio 10
### Concatenación de listas de caracteres
```python
from functools import reduce


lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']

def reduce_list(acc, value):
    acc.append(value)
    return acc

print(
        reduce(
            reduce_list,
            lista2,
            reduce(
                reduce_list,
                lista1,
                []
                )
            )
        )
```
## Ejercicio 12
### Calificación de alumnos
```python
from functools import reduce
lista1 = [1, 2]
lista2 = [3, 4]
def reduce_list(acc, value):
    acc.append(value)
    return acc
print(
        reduce(
            reduce_list,
            map(
                lambda x: (2, x),
                lista2
                ),
            reduce(
                reduce_list,
                map(
                    lambda x: (1, x),
                    lista1
                    ),
                []
                )
            )
        )
```

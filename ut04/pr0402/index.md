## Ejercicio 1
```python
cadena = input("Introduce una cadena: ")
consonantes = 0
vocales = 0
def is_vowel(char: str) -> bool :
    char = char.lower()
    if (char == 'a'):
        return True
    if (char == 'e'):
        return True
    if (char == 'i'):
        return True
    if (char == 'o'):
        return True
    if (char == 'u'):
        return True
    return False


for c in cadena:
    if (not c.isalpha()):
        continue
    if (is_vowel(c)):
        vocales += 1
        continue
    consonantes += 1


print(f'Numero de consonantes: {consonantes}')
print(f'Numero de vocales: {vocales}')
```
## Ejercicio 2
```python
print(input("Introduce una cadena: ")[::-1])
```
## Ejercicio 3
```python
cadena = input("Introduce la cadena para verificar si es un palindromo: ").lower()
print(f"Es palindromo: {"Si" if cadena == cadena[::-1] else "No"}")
```
## Ejercicio 4
```python
def contar_palabra(cadena: str): print(f'La longitud es: {len(cadena.split())}')
contar_palabra(input("Introduce una frase para contar las palabras: "))
```
## Ejercicio 5
```python
cadena = input("Introduce la cadena para quitar caracteres repetidos: ")
cadena_sin_repetidos = ""
for c in cadena:
    if (c not in cadena_sin_repetidos):
        cadena_sin_repetidos += c
print(cadena_sin_repetidos)
```
## Ejercicio 6
```python
cadena = input("Introduce la cadena: ")

minus = "abcdefghijklmnñopqrstuvwxyz"

cadena_result = ""
for i in cadena:
    if not i.isalpha():
        cadena_result += i
        continue
    if i in minus:
        cadena_result += i.upper()
        continue
    cadena_result += i.lower()

print(cadena_result)
```
## Ejercicio 7
```python
print(" ".join(input("Introduce una frase: ").split(" ")[::-1]))
```
## Ejercicio 8
```python
primera_cadena = input("Introduce la primera cadena: ")
segunda_cadena = input("Introduce la segunda cadena: ")
def anagrama(str1: str, str2: str) -> bool:
    if (len(str1) != len(str2)):
        return False
    return str1.lower().split().sort() == str2.lower().split().sort()

print(f'Son anagramas: {'Si' if anagrama(primera_cadena, segunda_cadena) else 'No'}')
```
## Ejercicio 9
```python

```
## Ejercicio 10 
```python
string = input("Introduce la cadena: ")
result_string = ""
for i in string:
    if i.isalnum():
        result_string += i
print(result_string)
```
## Ejercicio 11
```python
string = input("Introduce la cadena: ")
camelCase = ""
upper = False
for i in string:
    if i == " " or i == "-":
        upper = True
        continue
    if upper:
        upper = False
        camelCase += i.upper()
        continue
    camelCase += i.lower()

print(camelCase)
```
## Ejercicio 12
```python
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
```
## Ejercicio 13
```python
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
```

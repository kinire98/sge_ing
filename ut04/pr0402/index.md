# Ejercicios cadenas
## Ejercicio 1
### Contar vocales y consonantes
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
### Invertir una cadena
```python
print(input("Introduce una cadena: ")[::-1])
```
## Ejercicio 3
### Verificar palíndromo
```python
cadena = input("Introduce la cadena para verificar si es un palindromo: ").lower()
print(f"Es palindromo: {"Si" if cadena == cadena[::-1] else "No"}")
```
## Ejercicio 4
### Contar palabras
```python
def contar_palabra(cadena: str): print(f'La longitud es: {len(cadena.split())}')
contar_palabra(input("Introduce una frase para contar las palabras: "))
```
## Ejercicio 5
### Eliminar caracteres repetidos
```python
cadena = input("Introduce la cadena para quitar caracteres repetidos: ")
cadena_sin_repetidos = ""
for c in cadena:
    if (c not in cadena_sin_repetidos):
        cadena_sin_repetidos += c
print(cadena_sin_repetidos)
```
## Ejercicio 6
### Mayúsculas y minúsculas 
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
### Invertir palabras de una cadena
```python
print(" ".join(input("Introduce una frase: ").split(" ")[::-1]))
```
## Ejercicio 8
### Anagrama
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
### Frecuencia de caracteres
```python
def frecuencia_caracteres(string: str) -> dict:
    dictionary = {}
    for c in string:
        dictionary[c] = dictionary.get(c, 0) + 1
    return dictionary
print(frecuencia_caracteres(input("Introduce una cadena para saber la frecuencia de caracteres: ")))
```
## Ejercicio 10 
### Quitar caracteres alfanuméricos
```python
string = input("Introduce la cadena: ")
result_string = ""
for i in string:
    if i.isalnum():
        result_string += i
print(result_string)
```
## Ejercicio 11
### Transformar a camelCase
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
### Codificación RLE (Run-Length Encoding)
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
### Decodificar RLE
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
## Ejercicio 14
### Formateo de cadenas con plantillas
```python
def replace_str(string: str, dictionary: dict) -> str:
    words = string.split(" ")
    for i in range(len(words)):
        if words[i][0] == "{" and words[i][-1] == "}":
            final_idx = len(words[i]) - 1
            words[i] = dictionary.get(words[i][1:final_idx], "")
    return " ".join(words)
print(replace_str("Hola, {nombre}", {"nombre": "Alba"}))
```
## Ejercicio 15
### Comparar cadenas por valor ASCII
```python
string1 = input("Introduce una cadena: ")
string2 = input("Introduce una segunda cadena: ")

string1_ord = 0
string2_ord = 0

for i in string1:
    string1_ord += ord(i)
for i in string2:
    string2_ord += ord(i)

if string1_ord > string2_ord:
    print("La primera cadena tiene un mayor valor total")
elif string1_ord < string2_ord:
    print("La segunda cadena tiene un mayor valor total")
else:
    print("Las dos cadenas tienen el mismo valor")
```
## Ejercicio 16
### Contar la longitud de palabra más larga
```python
string = input("Introduce una serie de palabras: ")
max_length = 0
for i in string.split():
    max_length = max(max_length, len(i))
print(max_length)
```
## Ejercicio 17
### Formatear número con separador de miles
```python
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
```
## Ejercicio 18
### Rotar caracteres de una cadena
```python
string = input("Introduce la cadena a rotar: ")
num_rot = int(input("Introduce el numero de veces a rotar la cadena: "))
num_rot = num_rot % len(string) # modulo para cuando se introduzca un numero mas grande que la cadena solo quede el numero de rotaciones reales
print(string[num_rot:] + string[:num_rot])
```
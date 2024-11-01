## Ejercicio 1
### Buscar valor en un diccionario
```python
dicti = {
        "Fresa": 5,
        "Pera": 7,
        "Manzana": 3,
}
fruta = input("Introduce el nombre de una fruta: ")
res = ""
if dicti.get(fruta, 0) != 0:
    res = f"El precio de la fruta es: {dicti.get(fruta, 0)}"
else:
    res = "La fruta no existe"
print(res)
```
## Ejercicio 2
### Contar elementos en un diccionario
```python
productos = {
"Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
"Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
"Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
"Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
"Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}
num_categorias = 0
total_productos = 0
categorias = []
for key, value in productos.items():
    num_categorias += 1
    total_productos += len(value)
    categorias.append(f"{key}: {len(value)}")
print(f"Numero de categorias: {num_categorias}")
print(f"Total de productos: {total_productos}")
print("Total por categoria: ")
print("\n".join(categorias))
```
## Ejercicio 3
### Contador de frecuencia de palabras
```python
import re
file = open("./otono.txt")
file_content = re.split("\n|\\s|\\.|,|:|;", file.read())
file.close()
frecuencia_palabras = dict()
for word in file_content:
    if word == '':
        continue
    frecuencia_palabras[word] = frecuencia_palabras.get(word, 0) + 1
print(frecuencia_palabras.items())
```
## Ejercicio 4
### Diccionario de listas
```python
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}
print("Elige una opción: ")
print("1. Listar estudiantes matriculados en una asignatura")
print("2. Matricular un estudiante en una asignatura")
print("3. Dar de baja a un estudiante de una asignatura")
opcion = input("Elige lo que quieres hacer [1/2/3]: ")

while(opcion not in ["1", "2", "3"]):
    print("Elige una opción válida")
    opcion = input("Elige lo que quieres hacer [1/2/3]: ")

asignatura = input("Introduce una asignatura: ")
res = ""
if asignaturas.get(asignatura, 0) == 0:
    res = "No existe la asignatura"
else: 
    if opcion == "1":
        res = f"Alumnos matriculados en {asignatura}: {", ".join(asignaturas.get(asignatura, []))}"
    elif opcion == "2":
        alumnos = asignaturas.get(asignatura, [])
        alumnos.append(input(f"Introduce el nombre del alumno a matricular en {asignatura}: "))
    else:
        alumnos = asignaturas.get(asignatura, [])
        nombre_alumno = input("Introduce el nombre del alumno a desmatricular: ")
        if nombre_alumno in alumnos:
            alumnos = [i for i in alumnos if i != nombre_alumno]
            asignaturas[asignatura] = alumnos
        else:
            res = f"El alumno que has introducido no se encuentra matriculado en la asignatura: {asignatura}"
print(res)
if opcion != "1" and asignaturas.get(asignatura, []) != []:
    print(f"{asignatura}: ")
    print("\n".join(asignaturas.get(asignatura, [])))
```
## Ejercicio 5
### Diccionario invertido
```python
def invert_dictionary(dict_to_invert: dict) -> dict:
    inverted = dict()
    for key, value in dict_to_invert.items():
        inverted[value] = key
    return inverted
asignaturas = {
    "Matemáticas": "Ana",
    "Física": "Elena",
    "Programación": "Carlos",
    "Historia": "María",
    "Inglés": "Sofía",
}
print(invert_dictionary(asignaturas)) # No se pueden introducir valores que no se puedan hashear -> listas, sets o diccionarios
```
## Ejercicio 6
### Combinar diccionarios
```python
def combinar_diccionarios(dict1: dict, dict2: dict) -> dict:
    dict_combinado = dict()
    for key, value in dict1.items():
        if dict2.get(key, 0) != 0:
            dict_combinado[key] = value + dict2.get(key)
            continue
        dict_combinado[key] = value
    for key, value in dict2.items():
        if dict1.get(key, 0) != 0:
            continue
        dict_combinado[key] = value
    return dict_combinado   

precios1 = {
        "Pera": 1,
        "Manzana": 3,
        "Kiwi": 7
}
precios2 = {
        "Manzana": 7,
        "Kiwi": 5,
        "Naranja": 8,
}
print(combinar_diccionarios(precios1, precios2))
```
## Ejercicio 7
### Filtrar claves y valores
```python
def filtar_por_salario(salarios: dict[str, float], umbral: float) -> dict:
    filtrado = dict()
    for key, value in salarios.items():
        if value >= umbral:
            filtrado[key] = value
    return filtrado

print(filtar_por_salario({
    "Juan": 1660,
    "Currito": 1100,
    "Jefaso": 2213412
    }, 1500))
```
## Ejercicio 8
### Anidación de diccionarios
```python
def mostrar_empleados(empleados: dict):
    for key, value in empleados.items():
        print(f"{key}: {value}")
def anadir_empleados(empleados: dict, nombre: str, funcion: str) -> bool:
    if empleados.get(nombre, 0) != 0:
        print(f"{nombre} ya trabaja en este departamento")
        return False
    empleados[nombre] = funcion
    return True
def eliminar_empleados(empleados: dict, nombre: str) -> bool:
    if empleados.get(nombre, 0) == 0:
        print(f"{nombre} no trabaja en este departamento")
        return False
    del empleados[nombre]
    return True
def mostrar_todos_empleados(empleados: dict):
    for key, value in empleados.items():
        print(f"Departamento {key}: ")
        for k, val in value.items():
            print(f"{k}: {val}")
def main(dptos: dict):
    print("Elige una opción: ")
    print("1. Listar empleados de un departamento")
    print("2. Inscribir empleado en un departamento")
    print("3. Echar a un empleado de un departamento")
    opcion = input("Elige lo que quieres hacer [1/2/3]: ")

    while(opcion not in ["1", "2", "3"]):
        print("Elige una opción válida")
        opcion = input("Elige lo que quieres hacer [1/2/3]: ")

    dpto = input("Introduce el nombre de un departamento: ")

    if dptos.get(dpto, 0) == 0:
        print("El departamento no existe")
        return
    match opcion:
            case "1":
                print(dptos[dpto])
                mostrar_empleados(dptos[dpto])
            case "2":
                if anadir_empleados(dptos[dpto], 
                                 input("Introduce el nombre del empleado: "),
                                    input("Introduce la funcion del empleado en el departamento: ")):
                    mostrar_todos_empleados(dptos)
            case "3":
                if eliminar_empleados(dptos[dpto],
                                      input("Introduce el nombre del empleado: ")):
                    mostrar_todos_empleados(dptos)
departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}
main(departamentos)
```
## Ejercicio 9
### Transformación de datos
```python
estudiantes = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}
medias_asignaturas = dict()
notas_alumnos = dict()
for key, value in estudiantes.items():
    notas_alumno = []
    for k, val in value.items():
        notas_alumno.append(val)
        asignatura = medias_asignaturas.get(k, {})
        if asignatura == {}:
            medias_asignaturas[k] = {
                    "nota_media": val,
                    "notas": val,
                    "num_notas": 1
                    }
        else:
            notas = asignatura.get("notas") + val
            num_notas = asignatura.get("num_notas") + 1
            asignatura["nota_media"] = notas / num_notas
            asignatura["num_notas"] = num_notas
            asignatura["notas"] = notas
            medias_asignaturas[k] = asignatura
    media_alumno = sum(notas_alumno) / len(notas_alumno)
    notas_alumnos[key] = sum(notas_alumno) / len(notas_alumno)
print(medias_asignaturas)
print(notas_alumnos)
```
## Ejercicio 10
### Contar palabras en un texto
# *Igual que el ejercicio 3*
```python
import re
file = open("./otono.txt")
file_content = re.split("\n|\\s|\\.|,|:|;", file.read())
file.close()
frecuencia_palabras = dict()
for word in file_content:
    if word == '':
        continue
    frecuencia_palabras[word] = frecuencia_palabras.get(word, 0) + 1
print(frecuencia_palabras.items())
```
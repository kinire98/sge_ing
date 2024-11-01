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

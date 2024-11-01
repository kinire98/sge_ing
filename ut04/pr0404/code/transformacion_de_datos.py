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

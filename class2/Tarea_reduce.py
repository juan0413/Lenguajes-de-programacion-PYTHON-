from functools import reduce

# Función para calcular el promedio de un estudiante
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Lista de estudiantes con sus notas
estudiantes = [
    {'nombre': 'Juan', 'notas': [90, 85, 88, 92]},
    {'nombre': 'María', 'notas': [87, 88, 85, 90]},
    {'nombre': 'Pedro', 'notas': [92, 85, 88, 90]}
]

# Función para obtener las notas de un estudiante
def obtener_notas(estudiante):
    return estudiante['notas']

# Función para calcular el promedio de todos los estudiantes
def promedio_total(estudiantes):
    # Obtener las notas de todos los estudiantes
    todas_las_notas = map(obtener_notas, estudiantes)
    # Calcular el promedio de cada estudiante
    promedios_estudiantes = map(calcular_promedio, todas_las_notas)
    # Calcular el promedio total usando reduce
    promedio_total = reduce(lambda x, y: x + y, promedios_estudiantes) / len(estudiantes)
    return promedio_total

# Calcular y mostrar el promedio total
print("El promedio genereal de los estudiantes es:", promedio_total(estudiantes))

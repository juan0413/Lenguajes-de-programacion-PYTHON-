# Definimos una función que filtra las edades menores que cierto umbral
def filtrar_edades(edades, umbral):
    return filter(lambda edad: edad < umbral, edades)

# Función para ingresar los datos de los estudiantes
def ingresar_datos_estudiantes():
    estudiantes = []
    while True:
        nombre = input("Ingrese el nombre del estudiante o 'fin' para terminar: ")
        if nombre.lower() == 'fin':
            break
        edad = int(input("Ingrese la edad de {}:".format(nombre)))
        estudiantes.append((nombre, edad))
    return estudiantes

# Solicitamos al usuario que ingrese los datos de los estudiantes
datos_estudiantes = ingresar_datos_estudiantes()

# Umbral filtrar las edades
umbral = 20

# Filtramos las edades utilizando la función de orden superior
edades_filtradas = list(filtrar_edades([edad for _, edad in datos_estudiantes], umbral))

# Imprimimos las edades filtradas
print("Edades filtradas menores a", umbral, ":", edades_filtradas)
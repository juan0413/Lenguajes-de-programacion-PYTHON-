
def calcular_promedio(notas):
    total = sum(notas)
    cantidad_notas = len(notas)
    return total / cantidad_notas

def ingresar_notas():
    notas = []
    while True:
        nota = input("Ingrese una nota (o 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        notas.append(float(nota))
    return notas

def main():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    print("Ingrese las notas del estudiante (ingrese 'fin' para terminar): ")
    notas_estudiante = ingresar_notas()

    promedio = list(map(calcular_promedio, [notas_estudiante]))[0]

    print(f"El promedio del estudiante {nombre_estudiante} es: {promedio}")

if __name__ == "__main__":
    main()




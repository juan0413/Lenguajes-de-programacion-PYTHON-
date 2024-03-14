#INVERTIR UNA LISTA DE OBJETOS
"""""
def invertir_lista_recursivamente(lista):
    # Caso base: si la lista es vacía o tiene un solo elemento, devuelve la lista tal cual
    if len(lista) <= 1:
        return lista
    else:
        # Llama recursivamente a la función con la lista sin el primer elemento
        # y concatena el primer elemento al final de la lista invertida
        return invertir_lista_recursivamente(lista[1:]) + [lista[0]]

# Ejemplo 
lista_original = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista_recursivamente(lista_original)
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
"""

"""""
##INVERTIR UNA CADENA
def invertir_cadena_recursivamente(cadena):
    # Caso base: si la cadena es vacía, devuelve la cadena vacía
    if len(cadena) == 0:
        return ""
    else:
        # Llama recursivamente a la función con la cadena sin el último carácter
        # y concatena el último carácter al resultado de la cadena invertida
        return cadena[-1] + invertir_cadena_recursivamente(cadena[:-1])

# Ejemplo de uso
cadena_original = "Hola juan"
cadena_invertida = invertir_cadena_recursivamente(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
"""""

#FIBONACCI
"""""   
def fibonacci_recursivo(n):
    # Caso base: si n es 0 o 1, el valor de Fibonacci es n
    if n <= 1:
        return n
    else:
        # Llama recursivamente a la función para los dos números anteriores
        # y suma sus resultados para obtener el número de Fibonacci para n
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Ejemplo 
n_terminos = 10
print("Serie de Fibonacci para los primeros", n_terminos, "términos:")
for i in range(n_terminos):
    print(fibonacci_recursivo(i), end=" ")
"""
#Ejercicio contar el numero de caracteres distintos de una cadena cualquiera

def contar_cadena (cadena):
    return len(set(cadena)) 

cadena = input("Ingrese la cadena: ")
cantidad_caracteres_distintos = contar_cadena(cadena)
print("La cantidad de caracteres distintos de la cadena es: ", cantidad_caracteres_distintos)


#Ejercicio de preparacion 

records_humedales = [
    {"nombre":"panamericano","area":200,"especies_a":[
        {"nombre":"iguana","ejemplares":200},
        {"nombre":"garzas","ejemplares":250}
    ],"estado_conserv":"bueno"},
    {"nombre":"lago de la babilla","area":200,"especiales_a":[
        {"nombre":"babilla","ejemplares":8},
        {"nombre":"garzas","ejemplares":100}
    ], "estado_conserv":"bueno"}
]

#CALCULAR, USANDO MAP, REDUCE, FILTER:

#(1) AREA TOTAL DE LOS HUMEDALES
area_total_humedales = sum(map(lambda x: x["area"], records_humedales))
#(2) FILTAR HUMEDALES CON UN TOTAL DE EJEMPLARES ANIMALES > 150
humedales_filtrados = list(filter(lambda x: sum(map(lambda y: y["ejemplares"], x["especie_a"])) > 150, records_humedales))
#(3) PROMEDIO DE NUMERO DE EJEMPLARES DE LOS HUMEDALES
promedio_ejemplares = sum(map(lambda x: sum(y["ejemplares"] for y in x["especie_a"]),records_humedales)) / len(records_humedales)



    
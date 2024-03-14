#uso de funciones de orden superior: map, filter, reduce



from functools import reduce
#funcion para el filter
def es_par(x):
    return x%2 == 0
#funcion para el reuce
def suma(a,b):
    return a+b
#funcion 
def concat(a,b):
    return str.join(a, " ",b)
#creacion de mil numeros
lista = list(range(1,1001,1))
print(lista)


#creacion de lista de numeros pares
lista_pares = list (filter ( es_par   , lista  ) )
print(lista_pares)

lista_pares = list (filter( lambda x:x%2 == 0  ,lista   ))
print(lista_pares)

sumatoria = reduce( suma, lista_pares)
producto = reduce( lambda x,y: x*y, lista_pares)
print(sumatoria)
print(producto)

#Ejercicio
lista_palabras = ["muchachos","años","despue","frente","al","peloton","de",
         "fusilamiento","el","coronel","Aurelio", "Buendia"]

texto = reduce( lambda x,y: x+" "+y  ,lista_palabras )
print(texto)



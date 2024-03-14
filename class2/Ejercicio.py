from functools import reduce 

estudiantes = [ 
    {"nombre": "kevin","edad": 22, "notas":[3.5,3.8,4.7]},
    {"nombre": "Sebastian","edad": 21, "notas":[3.6,3.7,4.8]},
    {"nombre": "Brayan","edad": 23, "notas":[4.5,3.8,4.5]},
    {"nombre": "Moises","edad": 23, "notas":[4.4,3.6,4.7]}         
]

#usar map para promedio 
lista = [3.0, 5.0, 4.5]
suma_lista = sum(lista)
prom_lista = suma_lista / len(lista)
print(suma_lista)
print(prom_lista)

promedios = list(map(lambda record: sum(record["notas"])/len(record["notas"]), estudiantes))
print(promedios)
#Filter filtro de edad 
edad = int(input("Ingrese la edad para filtrar:\n"))
lista_filtrada = list(filter( lambda rec: rec["edad"] >= edad  ,estudiantes))
print(lista_filtrada)


#reduce promedio general
promedio_general = reduce(lambda x,y: x+y ,promedios) / len(promedios)
print(promedio_general)




lista_filt = [8, 9, 20, 14]

## RECURSION EL PARADIGMA FUNCIONAL

def fun_sumalista_iter(lista):
    suma=0
    for n in lista:
        sum = sum+n
        return sum

#Funcion recursiva (Directa)
def fun_sumalista_rec(lista):
    if not lista:
        return 0
    else:
        return lista[0] + fun_sumalista_rec(lista[1:])
    
def fun_sumalista_rec_ht(lista):
    if not lista:
        return 0
    else:
        #separa la lista en un elemento inicial y el resto:
        head, *tail = lista
        return head + fun_sumalista_rec_ht(tail)

print(fun_sumalista_iter(lista_test))
print(fun_sumalista_iter(lista_test))
print(fun_sumalista_iter(lista_test))

lista2 = [1,1,1,1,1,1]

print(fun_sumalista_rec_ht(lista2))
#filtrar lista con los elementos > a limite 
def filtra_lista(lista_filt, limite):
    if not lista:
        return []
    else:
    
        head, *tail = lista

#EJERCICIOS:
#INVERTIR UNA LISTA DE OBJETOS


#INVERTIR UNA CADENA

#FIBONACCI       
    

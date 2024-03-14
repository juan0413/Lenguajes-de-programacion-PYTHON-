#FUNCION DE PRIMER ORDEN
#version1 como en algoritmos
"""""
def op1(   a,b  ):
    return a+b
def op2(a, b):
    return a*b

def op3(a, b):
    return a**b

def op4(a,b):
    return a-b


    

operacion = int(input("que operacion? 1-suma, 2-resta, 3-potencia :"))
val1 = int(input("ingrese valor 1: "))
val2 = int(input("ingrese valor 2: "))
"""

#version 2: guardamos en f referencia a la funcion elegida.
""""
if operacion == "1":
    f = op1
elif operacion == "2":
    f = op2
elif operacion == "3":
    f = op3
elif operacion == "4":
    f = op4
else:
    print("funcion no definida")
    
print(f"el resultado es: {(val1,val2)}")
"""

#version 3: con funciones lambda (anonimas)
"""""
if operacion == "1":
    f = lambda x,y: x+y
elif operacion == "2":
    f = lambda x,y: x*y
elif operacion ==  "3":
    f = lambda x,y: x**y
elif operacion == "4":
    f = lambda x,y: x-y
else: 
    print("Funcion no definida")
    
print(f"el resultado es: {f(val1,val2)}")
"""
"""""
#version 4: con listas de funciones:
list_func = [op1, op2, op3, op4]


#version 5: con arreglo de lambdas:
#                        f[0]                f[1]          f[2]                f[3]           
list_func_lambda = [ lambda x,y: x+y, lambda x,y: x*y, lambda x,y: x**y, lambda x,y: x-y]

#aplicar la funcion que esta almacenada en la lista:
print(f"el resultado es: {list_func[operacion-1](val1,val2)}") 

"""
#FUNCIONES DE ORDEN SUPERIOR#
#Version 6 usando map
#calculadora
val1 = int(input("ingrese valor 1: "))
val2 = int(input("ingrese valor 2: "))

lista_calcu = [lambda  x,y: x+y, lambda x,y: x-y, lambda x,y: x**y, lambda x,y: x*y]

resultado = map(lambda f: f(val1, val2) ,lista_calcu)

list_resutl = list(resultado)

print(f"el resultado es: {list_resutl}")

#devuelve un iterable
 


 
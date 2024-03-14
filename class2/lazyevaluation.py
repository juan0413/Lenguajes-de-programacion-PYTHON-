#funcion impaciente
def mult(n, m):
    mults=[  n for n in range(n+1) if n%m == 0  ]
    return mults

#funcion perezosa
def mult_lazy(n, m):
    num = 0
    while True:
        if num % m == 0:
            yield num
        num += 1

m = int(input("Ingrese m:"))
n = int(input("Ingrese el numero de terminos:"))

mults = mult(n,m)
gen_mul = mult_lazy(n,m)

first_100 = [  next(gen_mul) for _ in range(100)  ]
print(f"Primeros 100:\n{first_100}")
next_100 = [ next(gen_mul) for _ in range(100)]
print(f"Siguientes 100:\n{next_100}")
print(mults)

def lazy_sum(n):
    sum = 0.0
    while True:
        i += 1.0
        sum += 1/i
        yield sum

n = int(input("ingrese n"))

gen_sum = lazy_sum(n)
#list_aprox1 = [next(gen_sum) for _ in range(n) ]
aprox1 = next(gen_sum)
#list_aprox2 = [next(gen_sum) for _ in range(n) ]
aprox2 = sum(next(gen_sum))
print(f"Aproximacion con los primeros {n} = {aprox1}")
print(f"Aproximacion con los siguientes {n} = {aprox2}")




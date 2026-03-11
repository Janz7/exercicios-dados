# Ex 6

def filtrar_pares(*args) -> list:
    
    pares = []

    for n in args:
        if n % 2 == 0:
            pares.append(n)

    return pares

resultado = filtrar_pares(1,2,3,4,5,6,7,8,9,10)

for i in resultado:
    print(i)

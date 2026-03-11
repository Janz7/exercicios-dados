# Ex 7

def multiplicar(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    mult = 0

    count = 0

    for i in valores:
        if count == 0:
            mult = i
        else:
            mult *= i
        count += 1
    
    return mult

resultado = multiplicar(2, 6, 3, 4, 10)
print(resultado)

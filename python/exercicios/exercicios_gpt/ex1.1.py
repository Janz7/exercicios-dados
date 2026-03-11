# Ex 1

def somar_numeros(a:float, b:float, *args):
    valores = a + b + sum(args)
    return valores

resultado = somar_numeros(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
print(resultado)


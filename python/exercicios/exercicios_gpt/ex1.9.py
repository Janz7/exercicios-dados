# Ex 9

def somar_positivos(a: float, b:float, *args)->float:
    valores = [a, b] + list(args)
    somaPositivos = 0

    for n in valores:
        if n >= 0:
            somaPositivos += n
    
    return somaPositivos

resultado = somar_positivos(1, 2, 3, -1, -5, -1, 4)
print(f"Resultado da soma é = {resultado}")
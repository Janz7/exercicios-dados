# Ex 3

def calcular_media(a:float, b:float, *args)->float:
    media = (a + b + sum(args)) / (len(args) + 2)
    return media

resultado = calcular_media(10, 10, 10, 5, 4, 3, 7, 1.2) 
print(resultado)
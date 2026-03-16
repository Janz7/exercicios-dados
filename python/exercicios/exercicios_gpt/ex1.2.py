# Ex 2

def maior_num(a:float, b:float, *args):
    valores = [a, b] + list(args)
    maiorNum = valores[0]
    for i in valores:
        if i > maiorNum:
            maiorNum = i
    return maiorNum

resultado = maior_num(-1, -5, -3, -2)
print(f"O maior número é {resultado}")
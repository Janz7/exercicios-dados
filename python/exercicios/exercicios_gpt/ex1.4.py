# Ex 4

def contar_argumentos(*args)->int:
    count = len(args)
    return count

resultado = contar_argumentos("a", "b", "c", 1, 2, 3)
print(resultado)
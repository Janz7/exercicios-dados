# Ex 5

def juntar_palavras(*args)->str:
    
    ptemp = ""
    
    for palavra in args:
        ptemp += palavra + " "

    return ptemp

resultado = juntar_palavras("Meu", "nome", "é", "Eduardo!")
print(resultado)
count = 0
soma = 0
entrada = 0

while entrada != "":
    entrada = input("Adicione saldo em sua conta: ")
    if entrada.isnumeric and entrada != "":
        entrada = float(entrada)
        soma += entrada
    elif entrada != "":
        print("Você deve digitar apenas números!")

print("O resultado da soma total é =", soma)    

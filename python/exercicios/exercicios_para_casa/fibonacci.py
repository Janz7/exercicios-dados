fibonacci = [1, 1]

posicaoDesejada = input("Insira a posição desejada da Sequência de Fibonacci: ")
if posicaoDesejada.isnumeric() and posicaoDesejada != "":
    posicaoDesejada = int(posicaoDesejada)

    indice = 1
    while indice <= posicaoDesejada:
        fibonacci.append(fibonacci[indice] + fibonacci[indice - 1])
        indice += 1

    print(fibonacci)
    print("A posição", posicaoDesejada, "corresponde ao número", fibonacci[indice - 2])

else: 
    print("Você deve inserir apenas números INTEIROS!")
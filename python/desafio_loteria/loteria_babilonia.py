# Construa um programa que realiza o sorteio de um número entre 1 e 15.

# O usuário terá 3 chances de acertar o valor.

# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.

# Caso o usuário acerte, dê os parabéns.

def valida_entrada(indice:int) -> int:
    isValid = False

    while isValid == False:
        entrada = input(f"Digite aqui (tentativa {indice + 1}): ")

        try:
            entrada = int(entrada)

            if entrada >= 1 and entrada <= 15:
                isValid = True
                return entrada
            else:
                print("Você deve digitar apenas números no intervalo entre 1 e 15!")
            
        except ValueError:
            print("Você deve digitar apenas números INTEIROS!")


def compara_valores(entrada:int, indice:int):
    if(entrada == num_sorteado):
        print("Párabens! você acertou.")
        return True
    else:
        if 3 - indice == 0:
            print("Número errado! acabaram suas chances.")
        else:
            string = f"Número errado! você ainda tem {3 - indice} chances"
            maiorOuMenor = "maior" if entrada > num_sorteado else "menor"
            dica = f"DICA: O número que você digitou é {maiorOuMenor} que o número sorteado!"
            print(string)
            print(dica)


# Main

import random

num_sorteado = random.randint(1, 15)

print("Tente descobrir o número sorteado! (Entre 1 e 15)")

for i in range(3):
    entrada = valida_entrada(i)

    resultado = compara_valores(entrada, i + 1)

    if resultado:
        break

else:
    print("Infelizmente não foi dessa vez, mais sorte na próxima!")

print(f"O número sorteado era: {num_sorteado}")
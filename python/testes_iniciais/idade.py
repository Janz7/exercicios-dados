idades = []

entrada = 0

while entrada != "":
    entrada = input("Insira uma idade pra adicionar na lista: ")

    if entrada.isnumeric and entrada != "":
        entrada = int(entrada)
        idades.append(entrada)
    elif entrada.isalpha and entrada != "":
        print("Você deve digitar apenas números INTEIROS!")


soma = sum(idades)
maiorIdade = max(idades)
menorIdade = min(idades) 
qtdeIdades = len(idades)


print(idades)
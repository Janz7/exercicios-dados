nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

if idade.isnumeric and idade != "":
    idade = int(idade)

    print("Olá", nome, ", bom saber que você tem", idade, "anos. Boas vindas!")
else:
    print("Você deve inserir apenas números INTEIROS!")
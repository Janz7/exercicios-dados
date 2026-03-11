texto = """
Escolha sua água: 
(1) - Água mineral sem gás -> R$ 1.50
(2) - Água mineral com gás -> R$ 2.50
"""

print(texto)
numEscolha = int(input("Digite a sua escolha de água: "))

valor = 0

if numEscolha == 1:
    valor = 1.50
elif numEscolha == 2:
    valor = 2.50

qtdGarrafas = int(input("Quantas garrafas você vai querer? "))

valor *= qtdGarrafas


if numEscolha != 1 and numEscolha != 2:
    print("Digite um número válido!")
else:
    print("Sua conta deu R$:", valor)

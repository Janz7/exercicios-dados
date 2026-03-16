nome = input("Insira seu nome completo: ")
idade = input("Insira a sua idade: ")

if idade.isnumeric() and idade != "":
    idade = int(idade)
else:
    while idade.isnumeric() == False:
        print("Você deve inserir apenas dígitos no campo de idade!")
        idade = input("Insira sua idade: ")

    if idade.isnumeric() and idade != "":
        idade = int(idade)

pessoa = {
    "nome" : nome,
    "idade" : idade
}

for chave, valor in pessoa.items():
    print(chave, "->", valor)
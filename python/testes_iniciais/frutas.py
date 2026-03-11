frutas = {
    "maçã" : "R$: 1,50",
    "melancia" : "R$: 4,50",
    "kiwi" : "R$: 3,00",
    "abacaxi" : "R$: 4,00",
    "pêra" : "R$: 1,00",
    "banana" : "R$: 0,50"
}

entrada = input("Qual fruta você deseja consultar o valor? Digite aqui: ")
entrada = entrada.lower()

if entrada in frutas:
    print(frutas[entrada])
else:
    while entrada not in frutas:
        print("Você deve inserir uma fruta válida!!!")
        entrada = input("Digite aqui: ")
        entrada = entrada.lower()

    
    print(frutas[entrada])

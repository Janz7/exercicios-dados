fruta = input("Entre com a fruta que você deseja consultar: ")
fruta = fruta.lower()

frutas = {
    "maçã": "R$1,50",
    "banana": "R$2,75",
    "uva": "R$1,90",
    "pera": "R$1,25",
    "laranja": "R$0,65",
    "limão": "R$1,25",
    "goiaba": "R$2,15",
    "abacaxi": "R$3,20",
    "jaca": "R$5,80"
}

if fruta in frutas:
    print(frutas[fruta])
else:
    while fruta not in frutas:
        fruta = input("Insira uma fruta VÁLIDA: ")
        fruta = fruta.lower()
    print(frutas[fruta])



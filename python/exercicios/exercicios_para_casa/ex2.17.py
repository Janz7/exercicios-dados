palavra = input("Insira uma palavra: ")

palavra = palavra.lower()

palavraInvertida = palavra[::-1]

if palavra == palavraInvertida:
    print("É um Palíndromo!!!")
else:
    print("Não é um Palíndromo!")
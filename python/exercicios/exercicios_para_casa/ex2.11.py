fraseEntrada = input("Digite uma frase: ")

palavra = ""
count = 0

for letra in fraseEntrada:
    if count == 0:
        temp = ""

    if letra == " ":
        palavra += temp
        exit()
    else:
        temp += letra
        count += 1







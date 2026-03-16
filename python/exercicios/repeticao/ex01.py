palavra = input("Insira uma palavra: ")

count = 0
contadorDeA = 0

while count < len(palavra):
    if palavra[count] == "a" or palavra[count] == "A":
        contadorDeA += 1
    count += 1

print("O número de vezes que a letra a foi encontrada é =", contadorDeA)


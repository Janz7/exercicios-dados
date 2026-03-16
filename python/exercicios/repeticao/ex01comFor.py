# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Insira uma palabra: ")

contador = 0

for letra in palavra:
    if letra == "a" or letra == "A":
        contador += 1

print("Contagem de letras A:", contador)
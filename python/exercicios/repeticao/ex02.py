# Faça um programa que receba 4 alturas usando um laço de repetição 
# e realize a soma dessas alturas.

count = 1
soma = 0

while count <= 4:
    altura = float(input("Digite a altura: "))
    soma += altura
    count += 1

print("O resultado da soma das alturas é:", soma)
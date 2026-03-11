notas = []

i = 0
while i < 4:
    entrada = input("Digite a nota: ")
    if entrada.isnumeric() and entrada != "":
        entrada = float(entrada)
        notas.append(entrada)
        i += 1
    else:
        print("Você deve digitar apenas números!")

media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print("MÉDIA: ", media)
print("MENOR NOTA: ", menor)
print("MAIOR NOTA: ", maior)
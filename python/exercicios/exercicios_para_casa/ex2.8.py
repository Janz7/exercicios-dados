print("Para saber mais sobre sua situação acadêmica, insira suas notas conforme solicitado!")

notas = []

count = 1
while count <= 4:
    isValid = False
    while isValid == False:
        nota = input("Nota: ")
        try:
            nota = float(nota)
            notas.append(nota)
            isValid = True
            count += 1
        except ValueError:
            print("Você deve digitar apenas NÚMEROS!")

media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print("Média =", media)
print("Menor =", menor)
print("Maior =", maior)
nums = []

entrada = 0
count = 1

while entrada != "":
    isValid = False

    while isValid == False:
        entrada = input(f"Número {count}: ")

        if entrada == "":
            break

        try:
            entrada = float(entrada)
            nums.append(entrada)
            isValid = True
            count += 1
        except ValueError:
            print("Você deve digitar apenas números!!!")

isValid = False
procurar = 0

while isValid == False:
    procurar = input("Qual número você deseja procurar na lista? Digite aqui: ")

    try:
        procurar = float(procurar)
        isValid = True
    except ValueError:
        print("Você deve digitar apenas números!!!")

countEncontrados = 0

for n in nums:
    if n == procurar:
        countEncontrados += 1

print(f"O número {procurar} foi encontrado {countEncontrados} vezes na lista fornecida!")

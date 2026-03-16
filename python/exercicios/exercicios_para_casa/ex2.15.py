qtd = int(input("Qual o tamanho da sua lista? "))
listaNums = [0] * qtd

num = int(input("Qual número você deseja procurar?"))

i = 0
entrada = 0

while i <= len(listaNums) - 1:
    entrada = input("Digite um número inteiro: ")
    if entrada.isnumeric and entrada != "":
        entrada = int(entrada)
        listaNums[i] = entrada
        i += 1
    else: 
        print("Você deve digitar apenas números INTEIROS!")

contagemNum = 0
for n in listaNums:
    if n == num:
        contagemNum += 1

print("O número", num, "foi encontrado", contagemNum, "vezes!")
     

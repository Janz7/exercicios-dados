lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

maiorNum = 0
posicaoMaiorNum = 0
countPosicao = 0;
for n in lista:
    if n > maiorNum:
        maiorNum = n
        posicaoMaiorNum = countPosicao
    countPosicao += 1


menorNum = 0
posicaoMenorNum = 0
countPosicao = 0

for n in lista:
    if n < menorNum:
        menorNum = n
        posicaoMenorNum = countPosicao
    countPosicao += 1


print("O maior valor está na posição", posicaoMaiorNum)
print("O menor valor está na posição", posicaoMenorNum)
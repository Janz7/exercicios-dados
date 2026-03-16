caminho_137 = "/home/eduardo/exercicios-dados/python/simulacao_137/137.csv"

with open(caminho_137, mode="r") as open_file:
    linhas = open_file.readlines()

chaves = linhas[0].strip("\n").split(";")
pessoas = {}

for c in chaves:
    pessoas[c] = []

for linha in linhas[1:]:
    registro = linha.strip("\n").split(";")
    for i in range(len(registro)):
        pessoas[chaves[i]].append(registro[i])

print(pessoas)


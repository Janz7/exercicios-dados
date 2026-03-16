#%%

caminho_teste = "/home/eduardo/exercicios-dados/python/teste_arquivos/teste.csv"

with open(caminho_teste, mode="r") as open_file:
    linhas = open_file.readlines()

chaves = linhas[0].strip("\n").split(";")

pessoas = {}

for c in chaves:
    pessoas[c] = []


for l in linhas[1:]:
    conteudo = l.strip("\n").split(";")

    for i in range(len(chaves)):
        pessoas[chaves[i]].append(conteudo[i])

print(pessoas)
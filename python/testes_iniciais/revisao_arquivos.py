# caminho_arquivo = "/home/eduardo/exercicios-dados/python/testes_iniciais/historia.txt"

# open_file = open(caminho_arquivo)

# read_file = open_file.read()

# open_file.close()

# print(read_file)

# caminho_arquivo = "/home/eduardo/exercicios-dados/python/testes_iniciais/historia.txt"

# with open(caminho_arquivo) as open_file:
#     resultado = open_file.read()

# print(resultado)
#%%
caminho_arquivo = "/home/eduardo/exercicios-dados/python/testes_iniciais/dados.csv"

with open(caminho_arquivo) as open_file:
    read_file = open_file.readlines()

chaves = read_file[0].strip("\n").split(";")
pessoas = {}

for c in chaves:
    pessoas[c] = []

for lines in read_file[1:]:
    registro = lines.strip("\n").split(";")
    print(registro)
    for i in range(len(chaves)):
        pessoas[chaves[i]].append(registro[i])

print(pessoas)
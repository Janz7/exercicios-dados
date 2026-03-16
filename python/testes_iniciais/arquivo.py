# Versão considerada má prática!

# caminho_arquivo = "teo.py"

# open_document = open(caminho_arquivo)

# read_document = open_document.read()

# print(read_document)

# open_document.close()

# %%

path_document = "/home/eduardo/exercicios-dados/python/testes_iniciais/ola_mundo.py"

with open(path_document) as open_document:
    result = open_document.read()

print(result)

# %%

path_document = "historia.txt"

with open(path_document, mode="w") as open_document:
    open_document.write("Meu nome é Eduardo Janz!")
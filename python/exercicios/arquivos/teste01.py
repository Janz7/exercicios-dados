# %%

caminho_arquivo = "texto.txt"

open_file = open(caminho_arquivo)

ler_arquivo = open_file.read()

print(ler_arquivo)

open_file.close()
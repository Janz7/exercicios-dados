# %%

import requests
import json
from tqdm import tqdm
import pandas as pd

def validarEntradaCEP():
    while True:
        entrada = input("Digite o CEP a ser buscado: ")

        if entrada.isnumeric() and entrada != "" and len(entrada) == 8:
            return entrada
        elif entrada == "":
            return 0
        else:
            print("Você deve digitar o cep corretamente!!!")

ceps = []


while True:
    entrada = validarEntradaCEP()

    if entrada == 0:
        break
    else:
        ceps.append(entrada)

# Consultando os CEPs via API

url = "https://viacep.com.br/ws/{entradaCep}/json/"

# Lista de dicionários
resultados = []

# Percorrendo CEPs e fazendo uma request pra cada cep,
# depois transformando em json e adicionando em "resultados"

for c in tqdm(ceps):
    endereco = requests.get(url.format(entradaCep=c))

    if endereco.status_code == 200:
        enderecoJson = endereco.json()
        resultados.append(enderecoJson)

# Mostrando resultados
# for r in resultados:
#     for chave, valor in r.items():
#         print(f"{chave} -> {valor}")
#     print("\n")

dataframe = pd.DataFrame(resultados)

dataframe

# Salvando os endereços de "resultados" em um arquivo JSON.

# with open("exercicios-dados/python/apis/resultados.json", mode="w", encoding="utf-8") as open_file:
#     json.dump(resultados, open_file, indent=4, ensure_ascii=False)



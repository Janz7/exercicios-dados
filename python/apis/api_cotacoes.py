def validarEntrada(txt:str):
    while True:
        entrada = input(f"{txt}")

        if len(entrada) == 3 and entrada.isalpha():
            return entrada
        else:
            print("Por favor, insira uma moeda válida!!!")

import requests

url = "https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

str1 = "Para qual moeda você quer converter o Real? Insira a sigla dela aqui: "

entrada1 = validarEntrada(str1).upper()

response1 = requests.get(url.format(moeda=entrada1))

if response1.status_code == 200:
    resultado = response1.json()
    for i in resultado[f"{entrada1}BRL"]:

        if i == "name":
            nomeMoeda = resultado[f"{entrada1}BRL"][i].split("/")
            nomeMoeda = nomeMoeda[0]

        if i == "bid":
            formatado = float(resultado[f"{entrada1}BRL"][i])
            print(f"1 {entrada1} está valendo R$: {formatado:.2f}")
            print(f"1 BRL está valendo $: {(1 / formatado):.2f} {nomeMoeda} ({entrada1})")
elif response1.status_code == 404:
    print("A moeda que você digitou é invalida ou não está no banco de dados!!!")

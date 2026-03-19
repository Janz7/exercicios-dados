# %%

import requests

url = "https://api.balldontlie.io/ucl/v1/teams"
api_key = "2c25472d-fef6-4974-9502-8092e13ee7e5"

response = requests.get(url, headers={"Authorization":"2c25472d-fef6-4974-9502-8092e13ee7e5"})

if response.status_code == 200:
    resultado = response.json()
    for i in resultado["data"]:
        for chave, valor in i.items():
            if chave == "name" or chave == "abbreviation":
                print(f"{chave} -> {valor}")
else:
    print("Erro!")





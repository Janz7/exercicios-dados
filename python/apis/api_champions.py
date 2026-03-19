# %%

import requests

url = "https://api.balldontlie.io/ucl/v1/teams"
api_key = "2c25472d-fef6-4974-9502-8092e13ee7e5"

response = requests.get(url, headers={"Authorization":"2c25472d-fef6-4974-9502-8092e13ee7e5"})

if response.status_code == 200:
    resultado = response.json()
    for time in resultado["data"]:
        for chave, valor in time.items():
            print(f"{chave} -> {valor}")
else:
    print("Erro!")




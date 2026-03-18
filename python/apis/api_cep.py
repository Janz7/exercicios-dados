def validarEntradas():
    isValid = False

    while isValid == False:
        entrada = input("Digite um cep para localizar: ")
        
        if entrada.isnumeric() and entrada != "":
            return entrada
        elif entrada == "":
            return 0
        else:
            print("Entrada de CEP inválida!!!")
            


import requests

isValid = False
ceps = []

while True:
    entrada = validarEntradas()

    if entrada == 0:
        break
    else:
        ceps.append(entrada)


url = "https://viacep.com.br/ws/{entradaCep}/json/"

info = []

for c in ceps:
    response = requests.get(url.format(entradaCep=c))
    resultado = response.json()

    info.append(resultado)

print(info)




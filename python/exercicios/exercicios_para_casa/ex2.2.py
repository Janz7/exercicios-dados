# %%
def inputValidation(entrada:str)->float:
    isValid = False

    while isValid == False:
        entrada = input("Digite um número: ")
        try:
            entrada = float(entrada)
            isValid = True
            return entrada
        except ValueError:
            print("Você deve digitar apenas números!")

def oddOrEven(entrada:float)->str:
    if entrada % 2 == 0:
        return "É Par!"
    else: 
        return "É Ímpar!"

entrada = 0
entrada = inputValidation(entrada)

resultado = oddOrEven(entrada)

print(resultado)

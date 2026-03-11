entradaTempo = input("Entre com um número em segundos: ")

if entradaTempo.isnumeric() and entradaTempo != "":
    entradaTempo = int(entradaTempo)

    horas = int(entradaTempo / 3600)
    entradaTempo = entradaTempo % 3600

    minutos = int(entradaTempo / 60)
    entradaTempo = entradaTempo % 60

    segundos = entradaTempo

    print("O resultado em HH:mm:ss é:", horas, ":", minutos, ":", segundos)

else:
    print("Você deve digitar apenas números INTEIROS!")
# Mostrar os números divisiveis por x no intervalo de 0 a 100

num = input("Insira um número inteiro: ")
if num.isnumeric and num != "":
    num = int(num)

    for n in range(1, 101):
        if n % num == 0:
            print(n)
else:
    print("Você deve inserir apenas números INTEIROS!")


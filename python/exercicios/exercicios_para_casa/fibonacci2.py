fibonacci = []

indiceDesejado = int(input("Insira o índice desejado: "))

i = 0

while i < indiceDesejado:
    if i == 0 or i == 1:
        fibonacci.append(1)
        i += 1
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        i += 1

print(fibonacci)

print("Fibonacci na posição", indiceDesejado, "é igual a", fibonacci[indiceDesejado - 1])
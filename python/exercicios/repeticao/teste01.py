# Mostrar os números diviseveis por 4 no intervalo 4-100

num = 4

count = 1

print("Números divisiveis por", num, "no intervalo de 1 a 100")

while count <= 100:
    if count % num == 0:
        print(count)
    count += 1
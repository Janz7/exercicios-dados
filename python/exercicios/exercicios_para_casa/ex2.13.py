num = input("Insira um número: ")
num = int(num)

count = num

fatorial = 0;

while count >= 1:

    if count == num:
        fatorial = count
        count -= 1
    else:
        fatorial *= count
        count -= 1

print("Fatorial de", num, "é =", fatorial)
    
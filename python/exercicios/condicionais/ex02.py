print("Escolha seu sorvete: ")
print("1 - Casquinha")
print("2 - Cascão")
print("3 - Cestinha")

tipo = int(input("Digite o número da sua escolha: "))

print("Sabores: ")
print("- Morango")
print("- Creme")
print("- Chocolate")
saborSorvete = input("Digite o sabor do sorvete: ")

print("Sabor da cobertura: ")
print("- Caramelo")
print("- Morango")
print("- Chocolate")
print("- Sem cobertura")
saborCobertura = input("Digite o sabor da cobertura: ")


valorTipo = 0;

if tipo == 1:
    valorTipo = 1.00
elif tipo == 2:
    valorTipo = 2.50
elif tipo == 3:
    valorTipo = 4.00


valorCobertura = 0

if saborCobertura == "sem cobertura":
    valorCobertura = 0.00
else:
    valorCobertura = 1.50

valorTotal = valorCobertura + valorTipo 

print("Seu sorvete de", saborSorvete, "vai custar R$:", valorTotal)


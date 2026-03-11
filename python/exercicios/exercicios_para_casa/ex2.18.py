frase = 0

frases = {}

while frase != "":
    frase = input("Digite uma frase: ")

    if frase not in frases and frase != "":
        frases[frase] = 1
    elif frase != "":
        frases[frase] += 1

for frase, num in frases.items():
    print(f"{frase} -> {num}")


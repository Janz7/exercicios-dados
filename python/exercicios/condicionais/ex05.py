item = input("Qual item você deseja comprar? ")

match item:
    case "laranja":
        input("Seu item está na lista!")
    case "cerveja":
        input("Seu item está na lista!")
    case "miojo":
        input("Seu item está na lista!")
    case "carvao":
        input("Seu item está na lista!")
    case "picanha":
        input("Seu item está na lista!")
    case _:
        input("Seu item não está na lista! Escolha outro")
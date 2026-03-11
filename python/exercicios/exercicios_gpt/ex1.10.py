# Ex 10

def estatisticas(a: int, b:int, *args)->dict:
    valores = [a, b] + list(args)

    media = sum(valores) / len(valores)
    maior = max(valores)
    menor = min(valores)

    return {
        "media" : media,
        "maior" : maior,
        "menor" : menor
    }

resultado = estatisticas(10, 30, 45, 38)

for chave, valor in resultado.items():
    print(f"{chave} = {valor}")
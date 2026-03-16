# Ex 8

def apresentar_pessoa(nome:str, *args)->None:
    print(f"Nome: {nome}")
    print("Hobbies: ")
    count = 0
    for i in args:
        if count == len(args) - 1:
            print(f"{i}")
        else:
            print(f"{i}, ")
        
        count += 1

apresentar_pessoa("Eduardo", "Jogar", "Dormir", "Comer")
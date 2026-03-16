pessoa = {
    "nome" : "Eduardo",
    "sobrenome" : "Janz",
    "idade" : 21,
    "parentes" : [{"nome" : "Ruth", "idade" : 47, "parentesco" : "mãe"},
                  {"nome" : "Eduardo", "idade" : 51, "parentesco" : "pai"},
                  {"nome" : "Bernardo", "idade" : 13, "parentesco" : "irmão"}]
}

# %%

for i in pessoa:
    print(i,":", pessoa[i])

# %%

for item in pessoa.items():
    print(item)

# %%

for chave, valor in pessoa.items():
    print(chave, ":", valor)
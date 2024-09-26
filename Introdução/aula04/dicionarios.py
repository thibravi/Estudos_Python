#%%
# dicionários são conhecidos também como mapas

dados = {"nome":"Thiago",
         "sobrenome":"Bravi", 
         "idade":40,
         "jogos":["GOW", "Horizon","Spider-man"],
         "pets":[{"nome":"LukeSkywalker", "idade":2}, {"nome":"Poliana","idade":6}]
         }

nome = dados["nome"]

print(nome)
print(dados["pets"][0]["idade"])
# %%

dados.keys() #chaves dos dicionários
# %%
dados.values()
# %%
dados.items() # retorna os pares. ex.: chave e valor

# %%

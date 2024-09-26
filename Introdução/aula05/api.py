#%%
import requests
import pandas as pd

#%%

url = "https://api.opendota.com/api/heroes"

resposta = requests.get(url)

#%%

resposta.status_code

#%%

dados = resposta.json()
# o json é uma estrutura de dados em javascript que serve para compor listas e/ou dicionários

#%%

dados[0]

#%%

for i in dados:
    print (i['localized_name'])

#%%

pd.DataFrame(dados)

#%%

df = pd.DataFrame(dados)

df.to_csv("heroes_dota.csv", sep=";")
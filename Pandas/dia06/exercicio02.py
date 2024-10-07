# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome
# 
# dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}

#%%
import pandas as pd

dados = {"nome":["Téo", "Nah", "Napoleão"],
         "idade": [31, 32, 14]}

df = pd.DataFrame(dados)
df

#%%

sumario = df.describe()
sumario

#%%

media_idade = df["idade"].mean()
media_idade

#%%

ultimo_nome = df["nome"].tail(1)
ultimo_nome
# %%
import pandas as pd
# %%

# dicionário aberto com {} e dentro tem várias listas
data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2]
}

#%%
data["idade"][0]

# %%
# transformando em data frame
# um dataframe é um conjunto de séries
# dataframe é como se fosse um excel e a série seria a coluna ou linha
df = pd.DataFrame(data)
df

#%% 
#descobrindo o tipo
type(df["idade"])

#%%
df["idade"].iloc[0]

# %%
df['sobrenome'].iloc[0]

# %%
df.iloc[0]

# %%
df['idade']

# %%

df.index=[3,2,1,0]
df
# %%
df["idade"][0]

# %%
df.index

# %%
df.columns

# %%
# o info é um método
df.info(memory_usage='deep')

# %%
# o dtypes é um atributo
df.dtypes

# %%
# describe vai aplicar as estatísticas descritivas nas colunas númericas
df['peso'] = [80, 53, 65, 14]
df.describe()

#%%

sumario = df.describe()
#%% 
sumario['peso']['mean']

# %%
df.head(3)

# %%
df.tail(2)
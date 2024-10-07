# %%
import pandas as pd

# importando e já colocando o nome das colunas
df = pd.read_csv("../data/products.csv",
                 sep=";",
                 names=["Id", "Name", "Description"]
                 )

df

# %%
# renomeando as colunas
df = df.rename(columns={"Name":"Nome",
                        "Description":"Descricao"})

df
# %%

df.rename(columns={"Name": "Nome",
                   "Description": "Descricao"},
                   inplace=True)

df
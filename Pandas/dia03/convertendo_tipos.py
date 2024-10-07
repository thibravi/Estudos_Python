# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.dtypes

#%%
# convertendo o tipo int para str

df["Points"].astype(str)

# %%
# criando uma coluna nova e multiplicando por 2
df["Points_dobble"] = df["Points"] * 2

# %%
# convertendo para float
df[["Points", "Points_dobble"]].astype(float)

# %%
# aqui não consegue converter texto para número inteiro
df[["UUID", "Name"]].astype(int)

# %%

df["Lista"] = [[ 1,2 ] for i in df.index ]
df

# %%

df.dtypes
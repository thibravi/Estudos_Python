# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()

# %%
df.isna().sum()

# %%
df.isna().mean()

# %%
# preenche os valores nulos 
# df.fillna(0) preenche com 0
# no exemplo abaixo, preenche com a média
df.fillna({
        "idade": df["idade"].mean(),
        "renda":df["renda"].mean(),
        })

# %%
# se fizer só df.dropna() vai remover a linha inteira

df.dropna(subset=["idade", "renda"], how='any')

# %%
df.dropna(axis=1, thresh=3)
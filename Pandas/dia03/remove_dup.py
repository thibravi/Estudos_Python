# %%
import pandas as pd

#%%
data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32,33,2,33,31,32],
    "updated_at":[1,2,3,1,2,3]
}
data

# %%
df = pd.DataFrame(data)
df

#%%
# no drop_duplicates precisa usar o subset para especificar quais colunas devem ser consideradas duplicadas e o keep para manter a primeira linha
# antes disso seria interessante ordenar por data de atualização, nesse caso em específico
df = (df.sort_values(by="updated_at", ascending=False)
        .drop_duplicates(subset=["Nome", "Idade"], keep='first'))

df
# %%

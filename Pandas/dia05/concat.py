# %%

import pandas as pd

data_01 = {
    "id": [1,2,3,4],
    "nome":["Teo", "Mat", "Nah", "Mah"],
    "idade": [31,31,32,32]
}

df_01 = pd.DataFrame(data_01)
df_01

# %%

data_02 = {
    "id": [5,6,7,8],
    "nome":["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23,33,19,21]
}

df_02 = pd.DataFrame(data_02)
df_02

# %%
# serve para empilhar os dados
# poderia usar para empilhar planilhas? acho que sim
pd.concat([df_01, df_02]).reset_index(drop=True)

# %%

data_03 = {
    "sobrenome":["Calvo", "Silva", "Costa", "Souza"],
    "renda": [3100, 3100, 3200, 3200]
}
df_03 = pd.DataFrame(data_03).sort_values(['renda','sobrenome'], ascending=[False, True])

df_03

#%%
# teste adicionando mais uma linha somente em um dos dfs. o resultado é que no df menor, ele adiciona o nan nas colunas faltantes
data_03 = {
    "sobrenome":["Calvo", "Silva", "Costa", "Souza", "Bravi"],
    "renda": [3100, 3100, 3200, 3200, 3400]
}
df_03 = pd.DataFrame(data_03).sort_values(['renda','sobrenome'], ascending=[False, True])

df_03
# %%
# usando o concat eu posso escolher se vou empilhar na vertical ou horizontal
# o axis=1 empilha na horizontal
pd.concat([df_01, df_03], axis=1)
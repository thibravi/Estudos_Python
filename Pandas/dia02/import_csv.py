# %%

import pandas as pd

# %%
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

#%%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%
df_customers["Points"].describe()

# %%
# se fizer somente df_customers["Points"] > 1000 o resultado será boleano, fazendo conforme abaixo vai retornar as linhas verdadeiras conforme a condição

condicao = df_customers["Points"] > 1000
df_customers[condicao]

# %%
#pessoa com mais pontos
# df_customers["Points"].max() retorna somente o número max
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%

condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_1000_2000 = df_customers[condicao].copy()


# %%
df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
# %%
df_customers

# %%
# para acessar duas colunas
df_customers[["UUID", "Name"]]

# %%
# o columns é um atributo do meu dataframe e o tolist é um método... converti isso para uma lista e criei uma variável para isso
# nessa primeira parte eu só peguei o nome das colunas
colunas = df_customers.columns.tolist()
colunas.sort()

# alterando o formato do dataframe
df_customers = df_customers[colunas]
df_customers

# %%
# renomeando as colunas e passando um dicionário para renomear... nome antigo e nome novo
# o rename gera um df novo, não altera o df anterior
df_customers = df_customers.rename(columns={"Name": "Nome",
                                            "Points": "Pontos"})

df_customers

# %%
df_customers.rename(columns={"UUID":"Id"}, inplace=True)
df_customers
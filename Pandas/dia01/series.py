# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1) 
variancia

# %%
# pega uma lista já declarada e converte para séries e coloca dentro de uma variável nova
# Transformação para séries Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séries pandas
# Média
series_idades.mean()

# %%
# Variância
series_idades.var()

#%%
# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3o Quartil
series_idades.quantile(0.75)

# %%
# Sumarização
series_idades.describe()

# %%
# Dimensão da série
# É uma tupla que me diz quantas linhas a minha série tem
series_idades.shape

# %%
# Navegando na lisa
idades[0]

# %%
# Navegando na série
series_idades[3]

# %%
# Alterando index da série
series_idades.index = ['t', 'e', 'o', 'c']

# %%
# Navegando nos índices novos
series_idades['t']

# %%

series_idades.index = [40, 10, 30, 20]


# %%
series_idades[40]

# %%
#iloc garante que está pegando pela posição
# iloc é posição e loc é índice
series_idades.iloc[-1]

# %%
series_idades.iloc[2:4]

# %%
series_idades.iloc[0:2]

# %%
# o loc usa os próprios índices
series_idades.loc[40]

# %%
series_idades.name = 'idades'
series_idades

# %%
# como se fosse nomear uma coluna no excel
# quando eu crio a série (series_idades) eu já posso dar uma nome para ela. a série pd.Series vai ter o conjunto de dados (idades) que é uma lista e o nome dessa série é idades e atribuo isso a uma varável

series_idades = pd.Series(idades, name="idades")
series_idades
# %%

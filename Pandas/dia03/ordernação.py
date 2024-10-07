# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=';')
df

# %%
# aqui estou sobrescrevendo o df original quando faço df = df...
# outra opção é usar o inplace para sobrescrever: df.sort_values( by=["Points", ascending=False, inplace=True
                        # pra fazer esse sort eu preciso colocar dentro de uma lista []
df = (df.sort_values( by=["Points", "Name"],
                      ascending=[False, True] )
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))

df
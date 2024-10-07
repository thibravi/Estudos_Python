# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user['Points'].sum()

# %%
# aqui temos um loop percorendo cada um dos elementos do idcustomer de forma única e somando a pontuação 
# mas esse formato não seria o ideal, existe uma forma melhor abaixo usando o groupby
pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df["IdCustomer"]==i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%
# dessa forma o processamento fica até mais rápido
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()


#%%

df.groupby(["IdCustomer"])["Points"].sum()

# %%
# teste usando o sort
(df.groupby(["IdCustomer"])
    .agg({ "Points": 'sum',
           "UUID": "count",
           "DtTransaction": "max"})
    .reset_index()
    .sort_values(by="Points", ascending=False)
    )


#%%
(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())

# %%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days

# %%

(datetime.datetime.now() - df["DtTransaction"][0]).days

# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": ['max', recencia]
          })
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
    .reset_index())

#%%
import datetime

def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

# Agrupando, agregando e renomeando
df_agg = (df.groupby(["IdCustomer"])
            .agg({
                "Points": 'sum',
                "UUID": "count",
                "DtTransaction": ['max', recencia]
            })
            .rename(columns={
                "Points": "Valor",
                "UUID": "Frequencia",
                "DtTransaction": "UltimaData"
            })
            .reset_index()
         )

# Ordenando pela coluna de recência
df_agg = df_agg.sort_values(by=('UltimaData', 'recencia'), ascending=True)

df_agg

# %%

import pandas as pd
df = pd.read_excel("../data/transactions.xlsx")

# %%
# tratamento do df
df_last = (df.sort_values("DtTransaction", ascending=False)
             .drop_duplicates(subset=['IdCustomer'], keep='first'))

df_last['IdCustomer'].nunique()

# %%
# busca no df para ver qual era a última transação
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]

# %%
# busca no df para ver se bate
df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
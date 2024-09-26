
# y = f(x) = x + 10
# y = f(x) = x * x + 1

#%%
# assinatura da função
def funcao(x):
    res = x + 10
    return res

# invocação da função
y = funcao(20)
print(y)
# %%

# a e b são argunmentos e quando escrevemos desse jeito, são obrigatórios
def soma(a, b):
    return a + b

# não seria possível chamar apenas um argumento aqui
soma(10, 20)
# %%

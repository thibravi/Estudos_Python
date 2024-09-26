
#%%

idade = int(input("Entre com a sua idade: "))

# os : indicam o final na condição lógica do if
if idade < 18:
    print("Você é menor de idade")

elif idade > 90:
    print("Idade avançada")

else:
    print("Você é maior de idade")
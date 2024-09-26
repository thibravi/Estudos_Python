#%%

qtde = int(input("Digite a quantidade de repetições da mensagem: "))

count = 1
while count <= qtde:
    print("vai dar certo!")
    count += 1  # count = count + 1 


#%%

while True:

    senha = input("Digite a senha: ")
    if senha == ("123456"):
        print("Senha correta!")
        break
    
    else:
        print("Senha incorreta")

#%%
#continue

while True:

    senha = input("Digite a senha: ")
    if senha == ("123456"):
        print("Senha correta!")
        break
    
    elif senha == ("12345"):
        print("quase...")
        continue

    print("Senha incorreta!")
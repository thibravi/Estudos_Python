# loteria. usuário tentando adivinhar um número V3
# try except
#%%
numero_sorte = 7


for i in range(3):

    while True: # criando esse while (infinito) para que o usuário continue digitando
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break # quando sair do loop e passar dessa linha, break

        except ValueError:
            print("Eu pedi um número!")

    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor.")

    else:
        print("Você errou! Tente um número maior.")


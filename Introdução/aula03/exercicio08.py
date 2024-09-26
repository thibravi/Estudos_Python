#Faça um programa que conte quantas vezes a letra a aparece em uma palavra

palavra = input("Digite uma palavra: ")

palavra1 = palavra.lower()

qtde = 0

for i in palavra1:
    if i == "a":
        qtde += 1


print("A letra 'a' aparece", qtde,"x na palavra", palavra)

#%%
#outro método de contagem
palavra = 'banana'
palavra.count("a")

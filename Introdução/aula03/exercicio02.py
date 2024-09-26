#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

tipo_sorvete = input("Escolha o tipo do sorverte: [casquinha / cascão / cestinha] ")

sabor = input("Escolha o sabor do sorvete: [morango / creme / chocolate] ")

cobertura = input("Escolha a cobertura: [caramelo / morango / chocolate] ")

valor = 0

# tipo de sorvete
if tipo_sorvete == 'casquinha':
    valor = valor + 1.00
    #ou +=
elif tipo_sorvete == 'cascão':
    valor += 2.5

elif tipo_sorvete == 'cestinha':
    valor += 4.00

else:
    print("Escolha corretamente!")

# tipo de cobertura
coberturas = 'caramelo,morango,chocolate'

# cuidado com o in porque ele entende parte das palavras ex late in chocolate
if cobertura in coberturas:
    valor += 1.5

elif cobertura == '':
    pass
    

else:
    print("Escolha corretamente!")

print("Seu sorvete", tipo_sorvete, "de", sabor, "com cobertura de", cobertura, "custa: R$", valor)
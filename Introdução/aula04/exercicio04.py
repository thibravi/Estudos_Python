##Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
##Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

tipo_sorvete = input("Escolha o tipo do sorverte: [casquinha / cascão / cestinha] ").lower()
sabor = input("Escolha o sabor do sorvete: [morango / creme / chocolate] ").lower()
cobertura = input("Escolha a cobertura: [caramelo / morango / chocolate] ").lower()

valor = 0

# tipo de sorvete, usando um dicionário ao invés de vários ifs
sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00
}

valor += sorvetes[tipo_sorvete]

if tipo_sorvete in sorvetes:
    valor += sorvetes[tipo_sorvete]
else:
    print("Pedido errado. Peça novamente")

# tipo de cobertura, usando um dicionário ao invés de vários ifs
coberturas = {
    "caramelo": 1.5,
    "morango": 1.5,
    "chocolate": 1.5,
    "": 0
}

if cobertura in coberturas:
    valor += coberturas[cobertura]
else:
    print("Pedido errado. Peça novamente")

print("Seu sorvete", tipo_sorvete, "de", sabor, "com cobertura de", cobertura, "custa: R$", valor)
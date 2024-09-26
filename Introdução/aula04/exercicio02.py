#Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas

# inicia com uma lista vazia

alturas = [] 

# cria um laço de repetição, limitando em 4 entradas
# i = 0 depois i = 1 depois i = 2 depois i = 3
for i in range(4):
                # o f é a formatação de string, passando pra dentro dela no meio das chaves uma variável que está fora, o i
    a = int(input(f"Entre com a alturas em cm {i + 1}: "))
    alturas.append(a)

soma = sum(alturas)
print(soma)
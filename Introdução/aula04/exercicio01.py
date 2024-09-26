#Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas

# método inciante
# o exercício 2 é mais avançadp usando o for

a1 = int(input("Entre com a alturas em cm: "))
a2 = int(input("Entre com a alturas em cm: "))
a3 = int(input("Entre com a alturas em cm: "))
a4 = int(input("Entre com a alturas em cm: "))

alturas = [a1, a2, a3, a4]

soma = sum(alturas)

print(soma)
# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha

lista = ["laranja", "cerveja", "miojo", "carvão", "picanha"]

item = input("O que você quer comprar? [laranja, cerveja, miojo, carvão, picanha] ")

if item in lista:
    print("Boa! Prossiga com a compra.")

else:
    print("Puts! Item em falta.")
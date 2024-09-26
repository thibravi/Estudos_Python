import random

def check_input():
    try:
        return int(input("Entre com um número entre 1 e 15: "))
            
    except ValueError:
        return "Eu pedi um número!"
            
def check_interval(numero):
     """Checa se o número passado está entre o intervalo programado. numero: int"""
     return 1 <= numero <= 15
        

def valida_entrada():
    """Essa função valida a entrada do usuário para garantir integridade do nosso código"""
    while True: # criando esse while (infinito) para que o usuário continue digitando
        numero = check_input()
        if type(numero) != int:
             print(numero)
             continue
        if check_interval(numero):
            return numero
        

numero_sorte = random.randint(1,15)

for i in range(3):

    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor.")

    else:
        print("Você errou! Tente um número maior.")
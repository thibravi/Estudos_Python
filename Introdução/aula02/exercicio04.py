# faça um programa que calcule a raiz quadrada de um número e exiba o resultado

numero = int(input("Insira um número para calcular a raiz quadrada: "))
                   
raiz = round(numero ** 0.5,2)

print("A raiz quadrada de", numero, "é:", raiz)
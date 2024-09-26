# faça um programa que receba um número em segundos, converta esse número para hora, minuto e segundo

segundos = int(input("Entre com um número em segundo: "))

horas = segundos // (60*60) # horas inteiras

segundos = segundos % (60*60) # resto de segundos da divisão por hora

minutos = segundos // 60 # minutos inteiros 

segundos = segundos % 60 # resto de segundos da divisão por minuto

print(horas,minutos,segundos, sep=":")

# o sep é a concatenação do espaçamento entre os argumentos
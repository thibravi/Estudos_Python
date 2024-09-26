#%%

arquivo = open("arquivo.txt", 'a') # w para escrever e o a para não sobrescrever o texto e adicionar mais linhas

arquivo.write("teste2 de escrita")

arquivo.close()

#%%

arquivo = open("arquivo.txt", 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

print(type(conteudo))

#%%
arquivo = open("arquivo.txt", 'r')
conteudo = arquivo.readlines()
arquivo.close()

print(conteudo)

print(type(conteudo))

#%%
# é melhor usar o with porque ele abre e fecha o arquivo sozinho. do jeinto anterior precisa abrir e fechar

with open("arquivo.txt", 'r') as file:
    conteudo = file.read()

    print (conteudo)
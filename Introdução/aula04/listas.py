#%%
# o append só recebe um elemento

notas = []
nota = 7.75

notas.append(nota)

print(notas)

notas.append(10)
print(notas)

# add uma lista dentro de um lista
notas.append([5.75, 6.24])
print(notas)

# criou uma lista com 3 elementos
#[7.75, 10, [5.75, 6.24]]
#float, inteiro e lista

#%%
# melhor usar o extend 
notas = []
nota = 7.75

notas.append(nota)

print(notas)

notas.append(10)
print(notas)

# add uma lista dentro de um lista
notas.extend([5.75, 6.24])
print(notas)

#outra adição de lista
notas = notas + [10, 9.5]
print(notas)

# %%

nome = 'thiago'
nome_alto = nome.upper()
print(nome_alto)

# %%
# for com listas

nomes = ['thiago', 'filipe', 'maria']
for i in nomes:
    print(i.title())

nomes.extend(['josé', 'paulo'])
print(nomes)

# %%

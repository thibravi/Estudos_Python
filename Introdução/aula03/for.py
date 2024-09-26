#%%

for i in "Thiago Bravi":

    if i == "T":
        continue
    print(i)

#%%
        # se não colocar nada no start, vai ser sempre zero
seq = range(0, 10) # (start, stop); qtde = stop - start

for i in seq:
    print(i)

#%%

qtde = int(input("Repetir quantas vezes? "))

for i in range(qtde):
    
    print("bora jogar?")

#%%

for i in range(1,16):
    if i % 2 == 0:
        print(i)
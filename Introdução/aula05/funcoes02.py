#%%
# def soma(a=0, b=0, c=0):
def soma(*args): # o *args vai ficar capturando valores que vamos passando para a função 
    return sum(args)

soma(10, 20, 50)
# %%

def soma(*args): # poderia ser outro nome no lugar do args também, mas precisa do *
    total = 0

    for i in args:
        total += i
    return total

soma(10, 20, 50)
# %%

def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i

    elif op == "mult":
        total = 1
        for i in num:
            total *= i

    return total

operacao("mult",1,2,3,4,5,6,7,8,9,10)

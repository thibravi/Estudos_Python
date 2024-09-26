#%%

idade = int(input("Entre com a sua idade: "))

cnh = input("Você tem cnh? ")

if idade >= 18 and cnh == 'sim':
    print("Siga em frente!")

else:
    print("Preso em nome da lei!")

#%%
#true e false / 0 e 1

print("True e True = ", bool(1 * 1))
print("False e True = ", bool(0 * 1))
print("True e False = ", bool(1 * 0))
print("False e False = ",bool(0 * 0))


#%%

print("True ou True =", bool(1 + 1))
print("False ou True =", bool(0 + 1))
print("True ou False =", bool(1 + 0))
print("False ou False =",bool(0 + 0))
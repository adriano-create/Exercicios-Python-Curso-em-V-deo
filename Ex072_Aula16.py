lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')

'''for comida in lanche:
    print(f'Eu vou comer {comida}')
    print('='*20)'''

for cont in range(0, len(lanche)):
    print(f'Eu vou Comer {lanche[cont]}')
    print('='*20)

'''for pos, comida in enumerate(lanche):
    print(f'Comi pra {comida} na posição {pos}!')          # Os duas formas dão o mesmo resultado'''

print(sorted((lanche)))

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c) # ele irá juntar A e B
print(len(c)) # Ele irá contar quantos elemetos tem dentro de C
print(c.count(5)) # Ira contar quando 5 tem dentro de C
print(c)
print(c.index(5, 1))'''
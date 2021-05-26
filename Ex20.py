######## Lita Ranqueada de Nomes #######

from random import shuffle

n1 = str(input('Digite o nome do primeiro Bebum: '))
n2 = str(input('Digite o nome do Segundo Bebum: '))
n3 = str(input('Digite o nome do quarto Bebum: '))
n4 = str(input('Digite o nome do Quinto Bebum: '))

lista = [n1,n2,n3,n4]
shuffle(lista)

print('A Ranking soa mais Bebuns são: ')
print(lista)

########### Escolha de Aluno ##############
import random
print('Quem é o mais noia da banca, que ama uma farofa da 50?: ')
a1 = str(input('Digite o Nome do Primeiro Noia: '))
a2 = str(input('Digite o nome do Segundo Noia: '))
a3 = str(input('Digite o nome do Terceiro Noia: '))
a4 = str(input('Digite o nome do Quarto Noia: '))
a5 = str(input('Digite o nome do Quinto Noia: '))
a6 = str(input('Digite o nome do Sexto Noia: '))

lista = [a1,a2,a3,a4,a5,a6]
escolhido = random.choice(lista)
print(' O cara mais Noia da Banca é: {}'.format(escolhido))
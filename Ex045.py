print('-=-' * 20)
print('JOKENPÕ')
print('-=-' * 20)

from time import sleep
import random

a = str('pedra')
b = str('papel')
c = str('tesoura')
lista = [a,b,c]
pc = random.choice(lista)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print(''' 
[1] para pedra.  
[2] para pepel.  
[3] para tesoura''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('Voccê escolheu pedra')
elif opcao == 2:
    print('Voccê escolheu Papel')
elif opcao == 3:
    print('Voccê escolheu Tesoura')



if (pc == a) and (opcao == 1 ):
    print('EMPATE!! computador também escolheu {} '.format(pc))
elif (pc == a) and (opcao == 2):
    print('Voce ganhou!! computador escolheu {} '.format(pc))
elif (pc == a) and (opcao == 3):
    print('O computador ganhou, escolheu {} '.format(pc))

elif (pc == b) and (opcao == 2):
        print('EMPATE, o computador também escolheu {}'.format(pc))
elif (pc == b) and (opcao == 1):
        print('O computador ganhou, escolheu {} '.format(pc))
elif (pc == b) and (opcao == 3):
        print('Voce ganhou, escolheu {}'.format(pc))

elif (pc == c) and (opcao == 3):
        print('EMPATEPC, computador também escolheu {} '.format(pc))
elif (pc == c) and (opcao == 1):
        print('Voce ganhou, computador optou por {} '.format(pc))
elif (pc == c) and (opcao == 2):
        print('O computador ganhou, comutador escolheu {} '.format(pc))













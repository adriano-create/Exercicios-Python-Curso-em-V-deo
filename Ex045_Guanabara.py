from random import randint
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''Suas Opções:
[0] PEDRA
[1] PEPEL
[2] TESOURA ''')
jogador = int(input('Qual a sua jogada: '))
print('.' * 30)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('.' * 30)

if computador == 0: # coputador jogou PEDRA#
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA! ')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA! ')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVALIDA! ')
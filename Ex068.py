from random import randint
from time import sleep
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite sua jogada: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Computador jogou {computador} + Jogador {jogador}, Total de {total} ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!, deu par ')
            v += 1
        else:
            print('Você Perdeu, deu IMPAR')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu, deu impar!')
            v += 1
        else:
            print('Voçê perdeu, deu PAR')
            break
    print(f'Vamos jogar novamente? voce tem {v} vitória(s)')
print(f'GAME OVER, Meu Amorzinho venceu {v} vez(es)')




import random

tentativas = 0
pc = random.randint(1, 10)
acertou = False
while not acertou:
    jogador = int(input('Adivinhe de 0 a 10 que o PC pensou: '))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente de novo.')
        elif jogador > pc:
            print('Menos... Tenta de novo')

print('Computador pensou em {} e suas tentativas {}'.format(pc, tentativas))
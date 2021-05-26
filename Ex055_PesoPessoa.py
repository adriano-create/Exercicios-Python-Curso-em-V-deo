print('='*20)
print(' Peso se pessoas, quem é a mais pesada e a mais leve .')
print('='*20)


maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso lido foi  {}kg'.format(maior))
print('O MENOR lido foi {}kg'.format(menor))

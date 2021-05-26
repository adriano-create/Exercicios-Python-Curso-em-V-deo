print('='*20)
print('NUMEROS PRIMOS')
print('='*20)

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ') # se for divisível,
        tot += 1
    else:
        print('\033[m', end=' ') # \033 corta a cor, se n for divisivel pela variavel a cor é a nativa
    print('{}'.format(c), end=' ')   ## Lembrando que end=' ', faz com que mostre o resultado na mesma linha
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print(('Ele é DIVISÍVEL 2x, então É PRIMO!'))
else:
    print('E por isso ele NÃO É PRIMO')
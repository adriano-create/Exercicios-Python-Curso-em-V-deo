print('-=-' * 20)
print('Calculdora com estrutura de repetção')
print('-=-' * 20)

n = int(input('de qual numero você quer a taboada? :'))
for c in range(1,10 + 1):
    print('{} x {} é igual a: {}'.format(n, c, n*c))
print('FIM')



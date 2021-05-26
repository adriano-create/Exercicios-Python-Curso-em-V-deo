print('-=-' * 20)
print('Comparação entre dois números, identificaçao qual maior, menor ou se são iguais ')
print('-=-' * 20)

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

if a > b:
    print('O numero {} é maior que o {} '.format(a,b))
elif b > a:
    print('O {} numero é maior que o {} '.format(b,a))
else:
    print('Os numeros {} e {} são iguais'.format(a,b))
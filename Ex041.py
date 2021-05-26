print('-=-' * 20)
print('Confederaçao Nacional de Natação')
print('-=-' * 20)

from datetime import date
ano = int(input('Digite o ano de Nascimento: '))
atual = date.today().year

idade = atual - ano

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade < 14:
    print('INFANTIL')
elif idade > 14 and idade < 19:
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')
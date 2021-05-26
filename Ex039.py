print('-=-' * 20)
print('Alistamento Militar ')
print('-=-' * 20)

from datetime import date
ano = int(input('Informe o ano do seu nascimento: '))


datual = date.today().year
idade = datual - ano

print(idade)
if idade < 16:
    print('Ainda vai se Alistar, faltam {} anos'.format(16 - idade))
elif idade >= 16 and idade <= 18:
    print('Esta na hora de se Alistar')
elif idade > 18:
    print('Já passou do prazo {} anos'.format(idade - 18))





print('-=-' * 20)
print('media de aluno ')
print('-=-' * 20)

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a Segunda nota: '))

media = (a + b) / 2

if media < 5:
    print('Sua media foi {:.1f} Você está REPROVADO: '.format(media))
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO {:.1f}'.format(media))
elif media > 7:
    print('Aprovado {:.1f}'.format(media))

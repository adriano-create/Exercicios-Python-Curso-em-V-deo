print('='*20)
print(' pessoas ainda não atingiram a maioridade e quantas já são maiores.')
print('='*20)

from datetime import date
dtual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    n = int(input('Digite o {} que nasceu: '.format(c)))
    idade = dtual - n
    if (dtual - n) < 18:
        menores += 1

    elif (dtual - n) > 18:
        maiores += 1
print('Ao todos tivemos {} pessoas maiores de idade '.format(maiores))
print('E também tivemos {} pessoas menores de idade '.format(menores))


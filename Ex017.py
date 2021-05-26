from math import hypot
co = float(input('Difite o cateto oposto: '))
ca = float(input('Digite o cateto Adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)


print('A Hipotenusa vai medir: ',hi)
print('A Hipotenusa vai medir: {} '.format(hi))
print('A hipotenusa vai medir {:.2f}'.format(hi))
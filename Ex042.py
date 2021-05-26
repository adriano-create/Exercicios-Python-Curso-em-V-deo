print('-=-' * 20)
print('Triangulo Escaleto, isoceles, Equilatero')
print('-=-' * 20)


r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
(r2 - r3) < r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2

if (r1 + r2) == (r1 + r3) == (r2 + r3):
    print('Triangulo Equilatero')
elif (r1 + r2) != (r1 + r3) != (r2 + r3):
    print('ESCALENO')
elif (r1 + r2) == (r1 + r2) != (r2 + r3):
    print('ISOCELES')
else:
    print('NÃO FORMA UM TRIANGULO')
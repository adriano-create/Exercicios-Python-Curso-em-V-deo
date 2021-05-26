km = float(input('Quantos km tem a viagem que fará?: '))
if km <= 200:
    pc1 = km * 0.50
    print('O valor total é de {} R$ já que sua viagem foi menos que 200 km'.format(pc1))
else:
    pc2 = km * 0.45
    print('Mais de 200 km a viagem, preço a pagar é: {}'.format(pc2))
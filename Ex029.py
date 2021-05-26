vel = float(input('Digite a velocidade do carro: '))
excesso = vel - 80
pagar = excesso * 7
if vel > 80:
       print('Excesso de velocidade, acima de 80 km/h, pagará multa de: {}'.format(pagar))
else:
       print('Boa viagem, coloque uma música pra relaxar')



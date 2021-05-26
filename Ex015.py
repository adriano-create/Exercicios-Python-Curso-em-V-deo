print(' Programa de Alugar de Carros ')

dias = int(input(' Quantos dias o carro foi alugado? '))
km = float(input(' Quantos Km o carro rodou? '))
valor = (dias*60)+(km*0.15)

print(' O valor total de aluguel de carro é R$: {:.2f}'.format(valor))

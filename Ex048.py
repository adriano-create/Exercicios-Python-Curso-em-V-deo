print('-=-' * 20)
print('Calcular numeros impares e calcular que são multiplos de 3 de 1 À 50')
print('-=-' * 20)

soma = 0
cont = 0
for c in range(1,501, +2):

    if (c % 3) ==0:
        cont = cont + 1
        soma += c
        # soma = soma + c
print('A Soma de todos {} os os solicitados é: {}'.format(cont,soma))

print('-=-' * 20)
print('IMC')
print('-=-' * 20)

a = float(input('Digite sua Altura: '))
p = float(input('Digite seu peso: '))
imc = p / (a ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Morbida')
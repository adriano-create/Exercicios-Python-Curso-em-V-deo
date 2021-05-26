extenso1 = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
extenso2 = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
extenso = extenso1 + extenso2

while True:
    numero = int(input('Digite um número de 0 a 20 para te-lo em extenso: '))
    if numero <= 0 or numero <= 20:
        break




'''for numero in range(0, len(extenso)):
numero = int(input('Digite um número para te-lo em extenso: '))
    print(extenso)'''
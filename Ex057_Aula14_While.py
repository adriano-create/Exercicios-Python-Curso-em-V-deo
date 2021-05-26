'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um Valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um Valor: '))
    if n != 0: # ae ele não conta o 0 como impar
        if n % 2 == 0:
            par +=1
        else:
            impar +=1

print('Qtd numeros pares {}, e Impares {}'.format(par,impar))



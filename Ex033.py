a = int(input('Digite primeiro numero: '))
b = int(input('Digite segundo numero: '))
c = int(input('Digite terceiro numero: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o numero maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    print('O maior valor digitadi foi {}'.format(maior))
    print('O menor valor digitadi foi {}'.format(menor))





'''if num1 > (num2 & num3):
    print('o maior numero é: ',num1)
if num2 > (num1 & num3):
    print('o maior numero é: ',num2)
if num3 > (num2 & num1):
    print('o maior numero é: ',num3)'''

'''while True:
    n = int(input('Digite um numero: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('FIM')'''

cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n < 0:
        break
    while cont < 10:
        cont +=1
        print(f'{n} x {cont} = {n * cont}')
    cont = 0
print('FIM')




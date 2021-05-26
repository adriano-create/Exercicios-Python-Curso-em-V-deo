n = soma = cont = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} e a soma é:  {soma}')

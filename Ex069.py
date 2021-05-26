menor = 0
m = 0
maior = 0

while True:
    tipo = ' '
    idade = int(input('Digite Idade: '))
    sexo = str(input('Digite Sexo [M/F]: ')).strip().upper()[0]
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F':
        if idade < 20:
            menor += 1
    if tipo == 'N':
        break


print(f'Total de pessoas com mais de 20 anos {maior}')
print(f'Quantos homens foram cadasrados {m}')
print(f'Mulheres menores de 18 anos {menor}')



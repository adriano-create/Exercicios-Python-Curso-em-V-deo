cont = maior = menor = total = totmil = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()[0]
    preco = int(input('Digite o preço do produto: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        cont += 1
        total = total + preco
    if preco > 1000:
       totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if continuar == 'N':
        break

print(f'O valor total dos produtos é {total:.2f}')
print(f'temos {totmil} que custam mais de R$1000.00')
print(f'o produto mais foi {barato} barato custa {menor}')
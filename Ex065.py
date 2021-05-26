
n = 'S'
cont = soma = media = maior = menor = 0
while n == 'S':
    r = int(input('Digite um número: '))
    cont += 1
    soma = soma + r
    media = soma / cont
    n = str(input('Deseja continuar (S/N] ?: ')).upper()
    if cont == 1:
        maior = menor = r
    else:
        if r > maior:
            maior = r
        if r < menor:
            menor = r

print('Você digitou {} vezes,  a soma é {} e a media é: {:.2f}'.format(cont, soma, media))
print('O MAIOR numero digitado é {} e o MENOR é: {}'.format(maior,menor))


from time import sleep
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
opcao = 0
while opcao != 5:
    print(''' n
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = a + b
        print('A soma entre {} e {} é: {}'.format(a, b, soma))
    elif opcao == 2:
        mult = a * b
        print('A Multiplicação de {} e {} é: {} '.format(a, b, mult))
    elif opcao == 3:
        if a > b:
            print('O maior numero é: {}'.format(a))
        elif b > a:
            print('O maior número é: {}'.format(b))
        else:
            print('Os numeros {} e {} são iguais'.format(a, b))
    elif opcao == 4:
        print('Quais são os novos números?')
        a = int(input('Digite primeiro valor: '))
        b = int(input('Digite segundo valor: '))
    elif opcao == 5:
        print('Finalizando programa...')
        sleep(2)
    else:
        print('Opção incorreta')

print('Fim do programa, volte smpre')


'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um Valor: '))
    if n != 0: # ae ele não conta o 0 como impar
        if n % 2 == 0:
            par +=1
        else:
            impar +=1'''
print('-=-' * 20)
print('Conversão INT para Binário, Octal e Exadecmal ')
print('-=-' * 20)

num = int(input('Digite um numero inteiro: '))
opcao = int(input('Digite "1" para Binário "2" para Octal e "3" para Exadecimal '))

if opcao == 1:
    print('Inteiro para binário é {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('Inteiro para Octal é {}'.format(oct(num)[2:]))
elif opcao == 3:
    print('Inteiro para Hexadecimal {}'.format(hex(num)[2:]))



print('{:=^40}'.format('Valor a ser pago por um produto'))


a = float(input('Qual o preço do produto? '))
print('Qual a condição de pagamento? ')
opcao = int(input('''FORMAS DE PAGAMENTO
[1] Diheiro/Cheque 10 % de desconto
[2] Cartão a vista à %5 de desonto 
[3] até 2x iguais sem juros
[4] 3x ou mais com 20% de juros: '''))

if opcao == 1:
    pagar = a - (a * 10 / 100)
    print('O valor a ser pago com 10% de desoconto é: {}'.format(pagar))
elif opcao == 2:
    pagar = a - (a * 5 / 100)
    print('O valor a ser pago com 10% de desoconto é: {}'.format(pagar))
elif opcao == 3:
    pagar = a / 2
    print('valor de cada parcela {:.2f} em 2x sem juros '.format(pagar))
elif opcao == 4:
    b = float(input('Quantas vezes?: '))
    pagar = a + (a * 20 / 100)
    parcelas = pagar / b
    print('O valor total R$ {:.2f}, parcelas de R$ {:.2f} em {:.1f}x'.format(pagar,parcelas,b))
else:
    opcao - a
    print('Errro, tente novante')



print('-=-' * 20)
print('Inicio Mundo 2')
print('Emprestimo para compra de uma casa')
print('-=-' * 20)

valor = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o seu salário R$: '))
anos = float(input('Em quantos anos você irá pagar?: '))
anos = anos * 12
prestacao = valor / anos


if prestacao > salario * 30 / 100:
    print('Infelizmente você é podre e não pode financiar essa casa! Prestação de {:.2f}'.format(prestacao))
else: print('Parabéns pela aquisção deste imóvél! prestação de {:.2f}'.format(prestacao))
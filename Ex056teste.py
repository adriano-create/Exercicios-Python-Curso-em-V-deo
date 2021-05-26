mulheresvelhas = 0
mediaidade = 0
homemvelho = 0
nomevelho = ''
somaidade = 0
for p in range(1, 5):
    print('===== {}° PESSOA ====='.format(p))
    nome = str(input('Digite o Nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o Sexo [M/F]'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
            homemvelho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
            mulheresvelhas += 1

mediaidade = somaidade / 4
print('media da idade do grupo {}'.format(mediaidade))
print('A idade do homem mais velho: {}, e ele se chama {}'.format(homemvelho, nomevelho))
print('Qtd de mulheres abaixo dos 20 anos: {}'.format(mulheresvelhas))





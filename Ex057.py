print(' ----- Progema só aceia M ou F ----- ')

sexo = str(input('Digite a porra do sexo: M ou F: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite novamente M ou F: ')).strip().upper()[0]
print('Sexo registrado com sucessso: {}'.format(sexo))

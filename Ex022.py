nome = str(input('Digite seu nome completo: ')).strip() #Não conta os espaços entes o depois do que foi digitado
print('Analisando seu nome ...')
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
print('Seu nome tem o total de letras é: {}'.format(len(nome)-nome.count(' '))) # Vai eliminar os espaços entre os nomes, assim, o programa contará só as letras dos nomes, e vai retirar espaços antes, depois ou entre eles
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # contará o primeiro espaço entre os nomes
separa = nome.split() # lembrando que o split cria uma lista / separa a os nomes
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[4], len(separa[0]))) #

# O split separou os nomes ex [Adriano, Batista] sendo que, "Adriano" começa em 0, logo depois o contador "len" controu o nome 0
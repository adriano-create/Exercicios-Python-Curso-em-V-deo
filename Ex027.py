nome = str(input('Digite seu nome Completo: ')).strip()
separa = nome.split()
print('Seu primeiro nome é {} e o seu ultimo nome é {} '.format(separa[0], separa[len(separa)-1]))

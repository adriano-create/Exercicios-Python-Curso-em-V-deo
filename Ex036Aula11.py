print('\033[4;31;46mOlá,Mundo! \033[m')

A = 2
B = 5
print('Valores \033[32m{}\033[m e \033[31m{}'.format(A , B))

nome = 'Adriano'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}
print('Muito prazer e te conhecer {}{}{} !!!'.format(cores['pretobranco'], nome, cores['limpa']))


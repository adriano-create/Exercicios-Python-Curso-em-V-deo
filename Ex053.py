print('='*20)
print('PALINDROMO')
print('='*20)



frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = '''
inverso = junto[::-1] # Macete do fatiamento no Python
print('Você digitou a frase {}'.format(junto))
'''for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]'''
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('Não forma um PALÍNDROMO')
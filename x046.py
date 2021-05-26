from time import sleep
import emoji
print('O ano novo começará em 10 segundos: ')
sleep(2)
for c in range(10,  -1, -1):
    sleep(1)
    print(c)
print('FELIZ ANO NOVO!!', end=" ")
print(emoji.emojize(':collision:'))


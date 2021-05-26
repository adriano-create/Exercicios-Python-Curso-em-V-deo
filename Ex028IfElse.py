import math
import random
from time import sleep
pc = random.randint(1,5)
print('-=-'*20)
num = int(input('Tente descobrir o numero de 1 a 5 que o computador pensou: '))
print('Processando...')
sleep(3)
if num == pc:
       print('Parabéns, você acertou',num)
else:
       print('ERrrrrrouuuuuuuu!! O pc pensou em {} e vc que é burro digitou {}'.format(pc,num))






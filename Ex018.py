################### Exercicio seno, coseno e tangente #######################

# import math
from math import radians, sin, cos, tan
a = float(input(' Digite o angulo que você deseja: '))
seno = sin(radians(a))
print(' O Angulo de {} tem o Seno de {:.2f}'.format(a,seno))
c = cos((radians(a)))
print(' O Angulo de {} tem o Cosseno de {:.2f}'.format(a,c))
t = tan(tan(radians(a)))
print(' O Angulo de {} tem a Tangente  de {:.2f}'.format(a,t))
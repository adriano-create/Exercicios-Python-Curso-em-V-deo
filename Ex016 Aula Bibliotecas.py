# from math import sqrt, math == importa apenas math e sqrt da biblioteca
# import randon ( Numero aleatório)


import emoji

import random
num = random.randint(1, 20)
print(num)

print(emoji.emojize("asdasd :earth_americas:", use_aliases=True))


nun = int(input(' Digite um Número: '))
raiz = math.sqrt(nun)
print(' A Raiz de {} é igual a {}'.format(nun,math.floor(raiz)))

print(' A Raiz de {} é igual a {}'.format(nun,math.ceil(raiz)))   # CEIL arredonda pra cima
print(' A Raiz de {} é igual a {}'.format(nun,math.floor(raiz)))  # FLOOR arredonda para caixo
print(' A Raiz de {} é igual a {:.2f}'.format(nun,raiz))          # {:.2f} Duas casas depois da virgula
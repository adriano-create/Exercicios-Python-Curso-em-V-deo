num = int(input("Digite um numero: "))
print('Analisando  o número: ',num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Undade: {} Dezena: {} Centena: {} Milhar {}'.format(u,d,c,m))





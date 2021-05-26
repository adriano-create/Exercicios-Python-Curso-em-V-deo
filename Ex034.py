sal = float(input('Qual é o salário?: '))
if sal > 1250:
    acre1 = sal * 0.10
    # Alternativa: acre1 = sal + (sal * 10 / 100)
    print('O seu salário com 10% de aumento por ser superior a 1250 é {:.2f}'.format(sal+acre1))
else:
    acre2 = sal * 0.15
    print('O Sálario por ser abaixo de 1250 recebe 15% de aumento: {:.2f}'.format(sal+acre2))
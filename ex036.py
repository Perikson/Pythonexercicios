vc = float(input('Qual o valor da casa: R$ '))
s = float(input('Qual o valor do seu salário: R$'))
a = int(input('Em quantos anos você vai pagar? '))
p = (vc / a) / 12

if p > (s * 30/100):
    print('Para pagar uma casa no valor de R$ {:.2f} em {:.0f} anos, a prestação será de R$ {:.2f}' .format(vc, a, p))
    print('Empréstimo Negado, a prestação está maior que 30% do seu salário.')

else:
    print('Para pagar uma casa no valor de R$ {:.2f} em {:.0f} anos, a prestação será de R$ {:.2f}' .format(vc, a, p))
    print('Empréstimo pode ser concedido')

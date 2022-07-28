print('{:=^40}' .format(' LOJAS PINHEIRO '))

v = float(input('Preço das compras R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] - à vista dinheiro/crédito - 10% de desconto.
[ 2 ] - à vista cartão - 5% de desconto.
[ 3 ] - 2x no cartão - sem juros.
[ 4 ] - 3x ou mais no cartão - 20% de juros.''')

opc = int(input('Digite a FORMA DE PAGAMENTO: '))

v1 = v - (v * (10/100))
v2 = v - (v * (5/100))
v4 = v + (v * (20/100))

if opc == 1:
    print('Sua compra no valor de R$ {:.2f} reais com 10% de desconto custará R$ {:.2f} reais.' .format(v, v1))
elif opc == 2:
    print('Sua compra no valor de R$ {:.2f} reais com 5% de desconto custará R$ {:.2f} reais.' .format(v, v2))
elif opc == 3:
    print('Sua compra no valor de R$ {:.2f} reais será parcelada em 2x de R$ {:.2f} reais.' .format(v, v/2))
elif opc == 4:
    p = int(input('Em quantas parcelas: '))
    print('Sua compra no valor de R$ {:.2f} reais será parcelada em {} de R$ {:.2f} reais.' .format(v, p, v4/p))
    print('Sua compra de {:.2f} reais, custará {:.2f} reais no final.' .format(v, v4))
else:
    print('Opção inválida de pagamento, tente novamente.')
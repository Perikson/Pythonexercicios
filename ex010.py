n = float(input('Quanto dinheiro voce tem na carteira? R$: '))
nd = float(n/3.27)
print('Com R${} você pode comprar US${:.2f}' .format(n, nd))

# Pode ser escrito com apenas uma variável.

n = float(input('Quanto dinheiro você tem em cateira? R$ '))
print('Com R${}, você pode comprar US${:.2f}' .format(n, float(n/3.227)))
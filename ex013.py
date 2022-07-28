s = float(input('Qual é o Salário do Funcionário? R$: '))
ns = s + (s * 15/100)
print('Um Funcionário ganhava R$ {:.2f}, com 15% de aumento, passa a receber R${:.2f}' .format(s, ns))
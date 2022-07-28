#s = Salário do Funcionário.
s = float(input('Qual é o salário do funcionário? R$ '))
if s <= 1250:
    print('Quem ganhava R$ {:.2f} reais, passa a ganhar R$ {:.2f} reais.' .format(s, s + (s * (15/100))))
else:
    print('Quem ganhava R$ {:.2f} reais, passa a ganhar R$ {:.2f} reais.' .format(s, s + (s * (10/100))))


# Outra maneira de se fazer:
s = float(input('Qual é o salário do funcionário? R$ '))

if s <= 1250:
    novo = s + (s * (15/100))
else:
    novo = s + (s * (10/100))

print('Quem ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}' .format(s, novo))
d = int(input('Quantos dias alugados? '))
kmr = float(input('Quantos Km rodados? '))
total = (d * 60) + (kmr * 0.15)
print('O total a pagar é R$ {:.2f}' .format(total))
n = str(input('Digite seu nome completo: ')).strip()
nf = n.split()
print('Seu primeiro nome é {}.' .format(nf[0]))
print('Seu último nome é {}.' .format(nf[len(nf)-1]))
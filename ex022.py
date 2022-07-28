n = input('Digite seu nome completo: ')
nM = n.upper()
nm = n.lower()
nl = n.replace(' ', '')
nn = len(nl)
np = n.split()[0]
npn = len(np)
print('''Analisando seu nome...\nSeu nome em maiúsculas é {}.\nSeu nome em minúsculas é {}.
Seu nome tem ao todo {} letras.\nSeu primeiro nome é {} e ele tem {} letras.'''.format(nM, nm, nn, np, npn))

#Outra maneira de fazer:

n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(n.upper()))
print('Seu nome em minúsculas é {}.'.format(n.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(n) - n.count(' ')))
print('Seu primeiro nome é {} e possui {} letras.'.format(n.split()[0], n.find(' ')))


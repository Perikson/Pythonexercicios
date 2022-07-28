print('=' * 30)
print('{:^30}' .format('Analisador de Primos'))
print('=' * 30)

n = int(input('Digite um número: '))
t = 0

for a in range(1, n + 1):
    if n % a == 0:
        t += 1

print('O número {} é divisível  {} vezes.' .format(n, t))
if t == 2:
    print('O número {} é PRIMO.' .format(n))
else:
    print('O número {} NÃO É PRIMO.' .format(n))


#Também Pode ser Escrito da Seguinte forma:

print('=' * 30)
print('{:^30}'.format('Analisador de Primos'))
print('=' * 30)

n = int(input('Digite um número: '))
t = 0

for a in range(1, n + 1):
    if n % a == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(a), end='')

print('\033[m\nO número {} é divisível  {} vezes.'.format(n, t))
if t == 2:
    print('O número {} é PRIMO.'.format(n))
else:
    print('O número {} NÃO É PRIMO.'.format(n))
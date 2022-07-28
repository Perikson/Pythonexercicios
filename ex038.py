n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('Primeiro número: {}' .format(n1))
print('Segundo número: {}' .format(n2))

if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO VALOR é maior.')
else:
    print('O dois valores são iguais.')

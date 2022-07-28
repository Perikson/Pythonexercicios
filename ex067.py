n = int(input('Quer ver a tabuada de qual valor: '))
print('{}' .format('---' * 12))

while True:
    for t in range(1, 11):
        print(f'{n} x {t} = {n * t}')
    print('Para finalizar digite um número negativo.')

    n = int(input('\nQuer ver a tabuada de qual valor: '))

    if n < 0:
        break

    print('{}'.format('---' * 12))

print('Programa finalizado.')
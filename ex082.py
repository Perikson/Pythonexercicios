lista = []
lpar = []
limpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        lpar.append(n)
    elif n % 2 != 0:
        limpar.append(n)

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Você digitou os números: {lista}')
print(f'VocÊ digitou os números pares: {lpar}')
print(f'Você digitou os números ímpares: {limpar}')

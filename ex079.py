valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com Sucesso.')
    else:
        print('Valor repetido. Número não pode ser inserido.')

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'Você digitou os valores: {sorted(valores)}')
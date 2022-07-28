
r = ''
ci = cm = cf = 0

while r in 'S':
    print('-' * 30)
    print('{:^30}' .format('CADASTRE UMA PESSOA'))
    print('-' * 30)

    i = int(input('Idade: '))

    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)

    if i > 18:
        ci += 1

    if s == 'M':
        cm += 1

    if s =='F' and i < 20:
        cf += 1

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar: [S/N] ')).strip().upper()[0]

print(f'Total de {ci} pessoas com mais de 18 anos. ')
print(f'Ao todo, temos {cm} homens cadastrados.')
print(f'Temos {cf} mulheres com menos de 20 anos.')


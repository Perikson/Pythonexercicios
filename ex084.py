lst = []
dd = []
ma = me = 0

while True:
    dd.append(str(input('Nome: ')))
    dd.append(int(input('Peso: ')))
    if len(lst) == 0:
        ma = me = dd[1]
    else:
        if dd[1] > ma:
            ma = dd[1]
        elif dd[1] < me:
            me = dd[1]

    lst.append(dd[:])
    dd.clear()
    r = str(input('Quer continuar? [S/N]'))
    if r == 'n':
        break
print(f'foram cadastrados {len(lst)} pessoas.')

print(f'O maior peso foi {ma}, sendo:', end='')
for p in lst:
    if p[1] == ma:
        print(f'[{p[0]}]', end='')

print(f'\nO menor peso foi {me}, sendo:', end='')
for p in lst:
    if p[1] == me:
        print(f'[{p[0]}]', end='')

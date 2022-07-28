num = []
c = 0
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    c += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
num.sort(reverse=True)
print(f'VocÊ digitou {c} números.')
print(f'A lista de números em ordem decrescente é :{num}')
if 5 in num:
    print('O valor 5 está na lista.')
else:
    print('Não existe valor 5 na lista.')

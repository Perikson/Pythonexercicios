print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)

r = ''
cs = cc = menor = c = 0
produto = ' '

while r in 'S':

    p = str(input('Produto: '))
    v = float(input('Preço: '))
    cs += v

    if v > 1000:
        cc += 1

    c += 1
    if c == 1:
        menor = v
        produto = p

    elif v < menor:
        menor = v
        produto = p

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print(f'{"FIM DO PROGRAMA":-^30}')
print(f'O total da compra foi R$ {cs:.2f} reais.')
print(f'Temos {cc} produto(s) custando mais de R$ 1000.00 Reais.')
print(f'O produto mais barato foi {p} que custa {menor:.2f} reais.')

r = ''
n = c = s = maior = menor = 0

while r in 'S':

    c += 1
    n = int(input('Digite um número: '))

    if c == 1:
        maior = menor = n

    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    s += n

media = s / c
print('VocÊ digitou {} números e a média foi {:.2f}' .format(c, media))
print('O maior valor que vc digitou foi {} e o menor foi {}' .format(maior, menor))


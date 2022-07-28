def aumentar(p, t):
    r = p + (p * t / 100)
    return moeda(r)


def diminuir(p, t):
    r = p - (p * t / 100)
    return moeda(r)


def dobro(n):
    r = n * 2
    return moeda(r)


def metade(n):
    r = n / 2
    return moeda(r)


def moeda(preço, moeda = 'R$'):
    return(f'{moeda} {preço:.2f}'.replace('.',','))


def resumo(p, ta = 10, tr = 5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    #print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p)}')
    print(f'Metade do preço: \t{metade(p)}')
    print(f'{ta}% de aumento: \t{aumentar(p, ta)}')
    print(f'{tr}% de redução: \t{diminuir(p, tr)}')
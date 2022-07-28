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
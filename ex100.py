from random import randint

def sorteia(lista):
    for v in range(5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Sorteando os {len(lista)} valores da lista: {lista}')

def somapar(lista):
    print(f'Somando os valores pares de {lista}.', end='')
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f' Temos {s}')

números = []
sorteia(números)
somapar(números)
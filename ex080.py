lista = []

for v in range(0, 5):
    n = int(input('Digite um número: '))
    if v == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)

#Caso queira uma lista com um número indefinido de números:

lista = []
c = 0
while True:
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer adicionar outro valor? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
    c += 1
print(lista)

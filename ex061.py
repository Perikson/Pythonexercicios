pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 1

while c <= 10:
    print('{}' .format(pt), end='')
    print(' ➝ ', end='')
    c += 1
    pt += r

print('FIM')
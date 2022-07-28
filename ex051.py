print('=' * 30)
pa = ('10 TERMOS DE UMA PA')
print('{:^30}' .format(pa))
print('=' * 30)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
#Fórmuda do décimo termo de uma PA.
d = pt + (10) * r

for a in range(pt, d, r):
    print('{}' .format(a), end=' ➙ ')
print('Acabou')
from datetime import date
dh = date.today().year

menor = 0
maior = 0

for p in range(1, 8):
    dn = int(input('Digite a data de nascimento da {}ª pessoa: ' .format(p)))
    i = dh - dn
    if i < 21:
        menor += 1
    if i >= 21:
        maior += 1

print('Existem {} menor(es) de idade.' .format(menor))
print('Existem {} maior(es) de idade.' .format(maior))
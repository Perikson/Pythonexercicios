print('=' * 30)
print(f'{"BANCO PMP":^30}')
print('=' * 30)

s = int(input('Que valor você quer sacar? R$ '))
print('')

total = s
ced = 50
tced = 0

while True:
    if total >= ced:
        total -= ced
        tced += 1

    else:
        if tced > 0:
            print(f'Foram Sacadas {tced} cédulas de {ced} Reais.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tced = 0
        if total == 0:
            break


print(f'\n{" Tenha um bom dia e Volte Sempre. ":^30}')
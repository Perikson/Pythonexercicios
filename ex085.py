lst = [[], []]

for v in range(7):
    n = int(input('Digite o valor: '))
    if n % 2 == 0:
        lst[0].append(n)
    else:
        lst[1].append(n)
print(f'Os números pares são {sorted(lst[0])}.')
print(f'Os números ímpares são {sorted(lst[1])}.')

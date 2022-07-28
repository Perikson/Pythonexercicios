matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc = ma = 0

for l in range(3):
    for c in range(3):
        matriz [l] [c] = int(input(f'Digite o valor para [{l}, {c}] '))

for l in range(3):
    for c in range(3):
        print('[{:^5}]' .format(matriz [l] [c]), end=' ')
        if matriz [l] [c] % 2 == 0:
            sp += matriz [l] [c]
    print()

for l in range(3):
    sc += matriz [l] [2]

for c in range(3):
    if c == 0:
        ma = matriz [1] [c]
    elif matriz [1] [c] > ma:
        ma = matriz [1] [c]

print(f'O maior valor da linha dois é: {ma}.')
print(f'A soma dos valores da terceira coluna vale: {sc}.')
print(f'A soma dos valores pares digitado vale: {sp}.')


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz [l] [c] = int(input(f'Digite o valor para [{l}, {c}] '))

for l in range(3):
    for c in range(3):
        print('[{:^5}]' .format(matriz [l] [c]), end=' ')
    print()


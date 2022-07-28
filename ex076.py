itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Canetas', 22.30,
         'Livro', 34.90)

print('----' * 10)
print(f'{"LISTAGENS DE PREÇOS":^40}')
print('----' * 10)

for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}R$', end='')
    else:
        print(f'{itens[pos]:^10.2f}')

print('----' * 10)
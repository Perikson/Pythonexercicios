valores = []
for n in range(0, 5):
    valores.append(int(input(f'Digite um número na posição {n}: ')))
print(f'Você digitou os seguintes números: {valores}')

print(f'O maior valor digitado foi {max(valores)} e foi digitado nas posições ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}...', end='')

print(f'\nO menor valor digitado foi {min(valores)} e foi digitado nas posições ', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}...', end='')


valores = []
vmax = []
vmin = []

for n in range(0, 5):
    valores.append(int(input(f'Digite o número da posição {n}: ')))
print(f'Os valores digitados foram: {valores}')

for pos, v in enumerate(valores):
    if v == max(valores):
        vmax.append(pos)

for pos, v in enumerate(valores):
    if v == min(valores):
        vmin.append(pos)

print(f'O maior valor digitado foi {max(valores)} e foi digitado nas posições: {vmax}')
print(f'O menor valor digitado foi {min(valores)} e foi digitado nas posições: {vmin}')

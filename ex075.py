vls = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))

print(f'Você digitou os valores: {vls}')

print(f'O valor 9 apareceu {vls.count(9)} vezes.')

if 3 in vls:
       print(f'O valor 3 apareceu na {vls.index(3) + 1}ª Posição.')
else:
       print('Não foi digitado o valor 3.')

print('Os valores pares digitados são: ', end='')
for p in vls:
       if p % 2 == 0:
              print(f'{p}', end=' ')

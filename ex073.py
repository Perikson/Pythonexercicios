tupla = ('Cotinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
     'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético',
     'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminese',
     'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
     'Atlético-GO')

print(f'Lista de times do Brasileirão: {tupla}', '\n')

print(f'Os 5 primeiros Colocados são: {tupla[:5]}', '\n')

print(f'Os quatro útimos são: {tupla[-4:]}', '\n')

print(f'Times em Ordem Alfabética :{sorted(tupla)}', '\n')

print(f'O Chapecoence está na posição {tupla.index("Chapecoense") + 1}', '\n')

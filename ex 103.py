def ficha(nom='<Desconhecido>', gol=0):
    print(f'O Jogador {nom} fez {gol} gols.')


n = str(input('Nome do Jogador: '))
g = str(input('Quantidade de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)


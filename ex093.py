dicio = {}
gols = []
dicio['Jogador'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dicio["Jogador"]} jogou? '))

for jogos in range(0, tot):
    gols.append(int(input(f'Quantos gols na partida {jogos + 1}? ')))

dicio['Gols'] = gols
dicio['Total'] = sum(gols)

print('=-=' * 20)
print(dicio)
print('=-=' * 20)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-=' * 20)

print(f'O Jogador {dicio["Jogador"]} jogou {tot} partidas.')
for p, g in enumerate(gols):
    print(f'- Na partida {p + 1}, fez {g} gols.')

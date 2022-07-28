jog = {}
gols = []
jogadores = []

while True:
    gols.clear()
    jog['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jog["Nome"]} jogou? '))

    for g in range(tot):
        gols.append(int(input(f'Quantos gols na partida {g + 1}? ')))

    jog['gols'] = gols[:]
    jog['Total'] = sum(gols[:])
    jogadores.append(jog.copy())

    while True:
        cont = str(input('Quer continuar? ')).strip().upper()[0]
        if cont in 'NS':
            break
        print(f'ERRO! Apenas S ou N.')
    if cont in 'N':
        break

print(f'{"Cod":^3}{"Jogador":^12}{"Gols":^16}{"Total":^10}')
for p, v in enumerate(jogadores):
    print(f'{p + 1:^3}{str(v["Nome"]):^10}{str(v["gols"]):^16}{str(v["Total"]):^10}')

while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar] '))

    if dados == 999:
        break

    else:
        if dados <= len(jogadores):
            print(f'O jogador {jogadores[dados - 1]["Nome"]} fez:')
            for p, n in enumerate(jogadores[dados - 1]['gols']):
                print(f'- No jogo {p + 1}, fez {n} Gols.')

        else:
            print(f'ERRO! Não existe jogador com o código {dados}')

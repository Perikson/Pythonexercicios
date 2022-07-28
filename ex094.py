dicio = {}
lista = []
pc = si = 0 # Pessoas Cadastradas e Soma de Idade
while True:
    pc += 1
    dicio['Nome'] = str(input('Nome: '))
    while True:
        dicio['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dicio['Sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    dicio['Idade'] = int(input('Idade: '))
    si += dicio['Idade']
    lista.append(dicio.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if cont in 'N':
        break

mi = si/pc # Média de Idade
print(f'Ao todo, temos {pc} pessoas Cadastradas.')
print(f'A média de idade é de {mi:.2f} anos.')

print('As Mulheres Cadastradas foram:')
for l in lista:
    if l['Sexo'] == 'F':
        print(f' - {l["Nome"]}')

print(f'Lista das pessoas que estão com a idade acima da média:')
for l in lista:
    if l['Idade'] > mi:
        print(f' - {l["Nome"]}')

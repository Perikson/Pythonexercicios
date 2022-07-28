lst = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lst.append([nome, nota1, nota2])
    c = str(input('Continuar? ')).strip().upper()[0]
    if c in 'N':
        break

print('-=-' * 20)
print('{:<5}{:<15}{:^10}' .format('Nº', 'Nome', 'Média'))
for i, l in enumerate(lst):
    print('{:<5}{:<15}{:^10}' .format(i + 1, l[0], (l[1] + l[2]) / 2))
print('-=-' * 20)
while True:
    opc = int(input('Deseja ver as notas de qual aluno? [999 para encerar] '))
    if opc == 999:
        break
    print(f'As notas de {lst[opc - 1][0]} são {lst[opc - 1][1]} e {lst[opc - 1][2]}.')
    print('-=-' * 20)

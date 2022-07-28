from datetime import date

n = int(input('Digite o Ano do Nascimento: '))
at = date.today().year
i = at - n

print('O atleta nascido em {}, possui {} anos.' .format(n, i))

print('-=-' * 8)

if i <= 9:
    print('Classificação: MIRIM.')
elif 9 < i <= 14:
    print('Classificação: INFANTIL.')
elif 14 < i <= 19:
    print('Classificação: JUNIOR.')
elif 19 < i <= 25:
    print('Classificação: SENIOR.')
else:
    print('Classificação MASTER.')

print('-=-' * 8)
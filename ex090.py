dict = {}

n = str(input('Nome do Aluno: '))
m = float(input('Média do Aluno: '))
dict['nome'] = n
dict['Média'] = m
if m <= 5:
    dict['situação'] = 'Reprovado'
elif m <= 7:
    dict['situação'] = 'Recuperação'
else:
    dict['Situação'] = 'Aprovado'

for k, v in dict.items():
    print(f'- {k} do aluno é {v}')

#também pode ser feito assim:

aluno = dict()

aluno['nome'] = str(input('Nome do Aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

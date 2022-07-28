from datetime import datetime
dicio = {}

dicio['Nome'] = str(input('Nome: '))
Nasc = int(input('Ano de Nascimento: '))
dicio['Idade'] = datetime.now().year - Nasc
dicio['Carteira de Trabalho'] = int(input('Carteira de Trabalho: (0 não tem) '))

if dicio['Carteira de Trabalho'] != 0:
    dicio['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dicio['Salário'] = int(input('Salário: '))
    dicio['Aposentadoria'] = dicio['Idade'] + ((dicio['Ano de Contratação'] + 35) - datetime.now().year)


for k, v in dicio.items():
    print(f' - {k} é {v}')


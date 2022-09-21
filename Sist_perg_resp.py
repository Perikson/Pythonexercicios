pr = {
    'Pergunta 1': {'Pergunta': 'Quanto é 2 + 2?', 'Resposta': {'a': '2', 'b': '4', 'c': '6', 'd': '8'},
                   'Resposta Certa': 'b'}}


for k, v in pr.items():
    print(f'{k}: {v["Pergunta"]}')

    for k1, v1 in v['Resposta'].items():
        print(f'[{k1}] = {v1}')

print()
for k, v in pr.items():
    print(f'A reposta correta da Questão 01 é a alternativa [{v["Resposta Certa"]}].')
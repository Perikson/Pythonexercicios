from random import randint
from time import sleep
from operator import itemgetter

jog = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
       'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
for k, v in jog.items():
    print(f'{k} rodou {v}.')
    sleep(1)

rank = []
rank = sorted(jog.items(), key=itemgetter(1), reverse=True)

print(f'{"RANKING":=^40}')
for p, v in enumerate(rank):
    print(f'{p+1}º lugar foi o {v[0]} e tirou {v[1]}.')
    sleep(1)


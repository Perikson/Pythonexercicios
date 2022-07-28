from random import randint

n = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))

print(f'Foram sorteados os valores: {n}')
print(f'Os valores em ordem: {sorted(n)}')
print(f'O maior valor foi: {max(n)}')
print(f'O menor valor foir: {min(n)}')

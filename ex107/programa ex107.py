from ex107 import moeda

n = float(input('Digite o preço: R$ '))
print(f'A metade de {n} é R$ {moeda.metade(n)}.')
print(f'O dobro de {n} é R$ {moeda.dobro(n)}.')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(n, 10)}.')
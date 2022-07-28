from ex109 import moeda

n = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}.')
print(f'O dobro de {moeda.moeda(n)} é R$ {moeda.dobro(n)}.')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(n, 10)}.')


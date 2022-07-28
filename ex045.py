from random import randint
from time import sleep

print('{:=^21}' .format(' Suas opções '))
print('''[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')

lista = ('PEDRA', 'PAPEL', 'TESOURA')
j = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)

print('=-=' * 5)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if j != 0 and j != 1 and j !=2:
    print('=-=' * 5)
    print('JOGADA INVALIDA \nJogue novamente')
    print('=-=' * 5)

else:
    print('=-=' * 5)
    print('O computador jogou {}.' .format(lista[pc]))
    print('Jogador jogou {}.' .format(lista[j]))
    print('=-=' * 5)

if j == 0: # Jogador jogou PEDRA.
    if pc == 0:
        print('EMPATE !!!')
    elif pc == 1:
        print('COMPUTADOR VENCEU !!!')
    elif pc == 2:
        print('JOGADOR VENCEU !!!')

elif j == 1: # Jogador jogou Papel.
    if pc == 0:
        print('JOGADOR VENCEU !!!')
    elif pc == 1:
        print('EMPATE !!!')
    elif pc == 2:
        print('COMPUTADOR VENCEU !!!')

elif j == 2: # PC Jogou Tesoura.
    if pc == 0:
        print('COMPUTADOR VENCEU !!!')
    elif pc == 1:
        print('JOGADOR VENCEU !!!')
    elif pc == 2:
        print('EMPATE !!!')






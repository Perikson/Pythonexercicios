from random import randint
from time import sleep # Dar uma ideia de que o computador está pensando.
computador = randint(0, 1) #Faz o computador sortear o número.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 1, tente adivinhar.')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(3)
print('Eu pensei no número {}.' .format(computador))
if computador == jogador:
    print('Parabéns, você acertou.')
else:
    print('Infelizmente você errou. Tente outra vez!')

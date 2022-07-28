from random import randint
pc = randint(0, 10)

print('-=-=' * 12)
print('''Olá, Sou seu computador. Vamos jogar um jogo?
Pensarei em um número entre 0 e 10. Tente adivinhar.''')
print('-=-=' * 12)

palpite = 0
j = 11

while pc != j:
    j = int(input('Qual o seu palpite: '))

    if j > pc:
        print('Menor...')
        print('Tente novamente.')
    elif j < pc:
        print('É Maior...')
        print('Tente novamente.')


    palpite += 1

print('PARABÉNS. O número que eu pensei foi {}.' .format(pc))
print('Voce tentou {} vezes.' .format(palpite))

# Outra maneira de escrever:

from random import randint

pc = randint(0, 10)
acertou = False
palpite = 0

print('''Olá, Sou seu computador. Vamos jogar um jogo?
Pensarei em um número entre 0 e 10. Tente adivinhar.''')

while not acertou:
    j = int(input('Qual o seu palpite: '))
    if j == pc:
        acertou = True

    else:
        if j < pc:
            print('É maior')
            print('Tente novamente.')
        elif j > pc:
            print('É menor.')
            print('Tente novamente.')

    palpite += 1

print('PARABÉNS. O número que eu pensei foi {}.' .format(pc))
print('Voce tentou {} vezes.' .format(palpite))

from random import randint
print('=-=' * 12)
print('{:^36}' .format('VAMOS JOGAR PAR OU IMPAR'))
print('=-=' * 12)
v = 0
while True:
    pc = randint(1, 10)
    n = int(input('Diga um Valor: '))

    j = ' '
    while j not in 'PI':
        j = str(input('Par ou Impar [P/I] ')).strip().upper()[0]

    s = pc + n
    print('O computador jogou {} e você jogou {}, a soma é {}.' .format(pc, n, s))
    pi = ' '
    if s % 2 == 0:
        if j == 'P':
            print(f'➝ {s} é PAR. Jogador Venceu !!!')
            v += 1
        else:
            print(f'➝ {s} é PAR. Jogador Perdeu !!!')
            break
    if s % 2 != 0:
        if j == 'I':
            print(f'➝ {s} é IMPAR. Jogador Venceu !!!')
            v += 1
        else:
            print(f'➝ {s} é IMPAR. Jogador Perdeu !!!')
            break
print(f'FIM DE JOGO. Você venceu {v} vezes.')

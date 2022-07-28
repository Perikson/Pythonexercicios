
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n = 0

while n != 5:
    print('''    [ 1 ] - Somar.
    [ 2 ] - Miltiplicar.
    [ 3 ] - Maior número.
    [ 4 ] - Novos números.
    [ 5 ] - Sair do Programa.''')

    n = int(input('Digite sua Opção: '))

    if n == 1:
        print('A soma de {} e {} vale {}.' .format(n1, n2, n1 + n2))

    elif n == 2:
        print('A multiplicação entre {} e {} vale {}.' .format(n1, n2, n1 * n2))

    elif n == 3:
        if n1 > n2:
            print('{} é o maior número.' .format(n1))

        elif n1 < n2:
            print('{} é o maior número.' .format(n2))

        elif n1 == n2:
            print('Os números são iguais.')

    elif n == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))

    elif n < 1 or n > 5:
        print('Opção incorreta. Tente novamente.')

print('Programa Encerrado. Até mais tarde.')



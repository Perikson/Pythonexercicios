def maior(* n):
    print('-=-' *15)
    print('Analisando os valores passados...')
    m = c = 0
    for v in n:
        c += 1
        print(f'{v} ', end='')
        if v > m:
            m = v
    print(f'\nForam informados {c} valores.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            break
        else:
            print('Digite um número válido.')
    return v


n = leiaint('Digite um valor: ')
print(f'O valor Digitado foi {n}.')
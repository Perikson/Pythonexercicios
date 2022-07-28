def leiadinheiro(msg):
    while True:
        p = str(input(msg)).strip().replace(',', '.').replace(' ', '')
        if p.isalpha() or p == '' or p.isalnum():
            print('Valor incorreto. Tente Novamente.')
        else:
            p = float(p)
            return p


def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            break
        else:
            print('Digite um número válido.')
    return v



def voto():
    from datetime import date
    print('-=' * 20)
    n = int(input('Ano de nascimento? '))
    i = date.today().year - n
    return i


idade = voto()
if idade < 16:
    print(f'Com {idade} anos. NÃO VOTA.')
elif idade < 18:
    print(f'Com {idade} anos. VOTO FACULTATIVO.')
else:
    print(f'Com {idade} anos. VOTO OBRIGATÓRIO.')

# TAMBÉM PODE SER ESCRITO DA SEGUINTE MANEIRA:

def voto(ano):
    from datetime import date
    atual = date.today().year
    i = atual - n
    if i < 16:
        return f'Com {i} anos. NÃO VOTA.'
    elif i < 18:
        return f'Com {i} anos. VOTO FACULTATIVO.'
    else:
        return f'Com {i} anos. VOTO OBRIGATÓRIO.'

n = int(input('Ano de nascimento? '))
print(voto(n))
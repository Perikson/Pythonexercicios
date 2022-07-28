somaidade = 0
nomevelho = ''
idadevelho = 0
m20 = 0

for pessoa in range (1, 5):
    print('----- {}ª Pessoa. -----' .format(pessoa))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += i

    if i > idadevelho and s == 'M':
        idadevelho = i
        nomevelho = n

    if i < 20 and s =='F':
        m20 += 1

media = somaidade / 4
print('A média das idades é {:.2f}' .format(media))

print('O Homem mais velho é {} e tem {} anos.' .format(nomevelho, idadevelho))

print('Existem {} mulher com menos de 20 anos.' .format(m20))
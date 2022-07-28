from time import sleep
def contador(i, f, p):
    print('-=-' * 15)
    print(f'Contador de {i} à {f} de {p} em {p}.')
    if i < f:
        while i <= f:
            sleep(0.5)
            print(f'{i} ', end='')
            i += p
        print('FIM')
    else:
        while i >= f:
            sleep(0.5)
            print(f'{i} ', end='')
            i += p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, -1)
print('-=-' * 15)
print('Agora é a sua vez...')
ini = int(input('Início: '))
fim = int(input('Fim: '))
temp = int(input('Tempo: '))
contador(ini, fim, temp)
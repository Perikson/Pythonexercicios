from time import sleep
n = int(input('Digite um número para o cálculo de seu Fatorial: '))
f = 1

print('Calculando o Fatorial de {}! ...' .format(n))
sleep(1)
while n >= 1:
    print('{}' .format(n), end='')
    if n > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= n
    n -= 1


print('{}' .format(f))
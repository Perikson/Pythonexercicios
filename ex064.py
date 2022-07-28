n = int(input('Digite um número [999 para parar]: '))
c = s = 0

while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))

print('você digitou {} números e a soma entre eles foi {}.' .format(c, s))

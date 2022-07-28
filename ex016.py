import math
num = float(input('Digite um valor: '))
print('O Valor digitado foi {} e sua porção inteira é {}.' .format(num, math.trunc(num)))

# usando apenas a função trunc

from math import trunc
num = float(input('Digite um valor: '))
print('O Valor digitado foi {} e sua porção inteira é {}.' .format(num, trunc(num)))


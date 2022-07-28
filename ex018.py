import math
an = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}.' .format(an, s))
print('O ângulo de {} tem o COSSENO de {:.2f}.' .format(an, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}.' .format(an, t))

# Usando apenas uma variável e o comando from () import ()

from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}.' .format(an, sin(radians(an))))
print('O ângulo de {} tem o COSSENO de {:.2f}.' .format(an, cos(radians(an))))
print('O ângulo de {} tem a TANNGENTE de {:.2f}.' .format(an, tan(radians(an))))

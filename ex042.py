n = ('Analisador de triângulos')
print('-=-' * 20)
print('{:^60}' .format(n))
print('-=-' * 20)

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 == r3:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO.')

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES.')

    else:
        print('Os segmentos acima podem formar um triângulo ESCALENO.')

else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
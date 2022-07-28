#O resto da divisão por 2 diz se um número é par ou impar. Se for 1 é impar ou se for 0 é Par.

n = int(input('Digite um número: '))
r = n % 2
if r == 1:
    print('O número {} é ÍMPAR.' .format(n))
else:
    print('O número {} é PAR.' .format(n))
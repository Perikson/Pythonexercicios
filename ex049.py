n = int(input('Digite o número para ver a tabuada: '))
for a in range(1, 11):
    print('{} x {} = {}.' .format(n, a, (n * a)))
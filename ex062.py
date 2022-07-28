pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 1

total = 0
mais = 10

while mais != 0:

    total += mais

    while c <= total:
        print('{} ➝ ' .format(pt), end='')
        c += 1
        pt += r

    print('Pausa')
    mais = int(input('Quantos termos a mais você quer ver? '))

print('Progressão Finalizada com {} termos mostrados.' .format(total))
print('FIM')
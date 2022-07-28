s = 0 #Acumulador.
c = 0 #Contador.
for a in range(1, 7):
    n = int(input('Digite o {} valor: ' .format(a)))
    if n % 2 == 0:
        s = s + n #tbm pode ser escrito como s += n
        c = c + 1 #tbm pode ser escrito como c += n

print('A soma dos {} números pares é igual a {}.' .format(c, s))


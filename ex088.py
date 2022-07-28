from random import randint
lst = []
temp = []
q = int(input('Quantos sorteios você quer? '))

for jogos in range(q):
    while True:
        n = randint(1, 60)
        if n not in temp:
            temp.append(n)
        if len(temp) >= 6:
            break
    lst.append(temp[:])
    temp.clear()

for j in lst:
    print('{}' .format(sorted(j)))

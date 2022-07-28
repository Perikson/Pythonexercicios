maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(pessoa)))

    if pessoa == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('O maior peso é {:.1f}' .format(maior))
print('O menor peso é {:.1f}' .format(menor))

#Também pode ser realizado da seguinte maneira.

lst = [] #lista vazia

for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(pessoa)))
    lst += [peso] #adc os valores de peso na lista

print('O maior peso é {:.1f}' .format(max(lst))) #maximo valor da lista
print('O menor peso é {:.1f}' .format(min(lst))) #minimo valor da lista
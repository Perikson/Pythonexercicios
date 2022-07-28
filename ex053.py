f = str(input('Digite uma frase: ')) .strip() .upper() #frase
p = f.split() #Palavras separadas
print('Você digitou a frase "{}"' .format(f))

j = ''.join(p) #junção da frase sem os espaços.
print('A frase junta é "{}"' .format(j))

i = '' #Inverso da palavra
for l in range(len(j) - 1, -1, -1): #l = letra.
    i += j[l]

print('A frase digitada no inverso é {}' .format(i))

if i == j:
    print('A frase é um Palíndromo.')

else:
    print('A frase não é um Palíndromo.')

#Também pode ser escreta da seguinte maneira:

f = str(input('Digite uma frase: ')) .strip() .upper() #frase
p = f.split() #Palavras separadas
print('Você digitou a frase "{}"' .format(f))

j = ''.join(p) #junção da frase sem os espaços.
print('A frase junta é "{}"' .format(j))

i = j[::-1] #Inverso da palavra
print('A frase digitada no inverso é {}' .format(i))

if i == j:
    print('A frase é um Palíndromo.')

else:
    print('A frase não é um Palíndromo.')

# Também pode ser escreta da seguinte maneira:

frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
print('-=' * 30)
print('''Digite o número que será convertido e escolha a conversão:
1 - Para Binário
2 - Para Octal
3 - Para Hexadecimal''')
print('-=' * 30)

# número que será convertido: n.
n = int(input('Digite o número: '))

#opção de conversão: oc.
oc = int(input('Digite a base de conversão: '))

#Conversão:
if oc == 1:
    print('O número digitado {} convertido para Binário vale {}' .format(n, bin(n)[2:]))
elif oc == 2:
    print('O número digitado {} convertido para Octal vale {}' .format(n, oct(n)[2:]))
elif oc == 3:
    print('O número digitado {} convertido para Hexadecimal vale {}' .format(n, hex(n)[2:]))
else:
    print('Digite uma base de conversão válida.')
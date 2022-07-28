t = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove'
     , 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete'
     , 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))

    if 0 <= n <= 20:
        break
    else:
        print('Tente novamnte. ', end='')

print('O Número digitado foi {}.' .format(t[n]))
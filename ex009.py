n = int(input('Digite um número para ver sua tabuada: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('n x 1  = {} \nn x 2  = {} \nn x 3  = {} \nn x 4  = {} \nn x 5  = {} \nn x 6  = {} \nn x 7  = {} \nn x 8  = {} \nn x 9  = {} \nn x 10 = {}' .format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))

#Também pode ser escrito assim:

n = int(input('Digite um número para ver sua tabuada: '))
print('{} x {:2} = {}' .format(n, 1, n*1))
print('{} x {:2} = {}' .format(n, 2, n*2))
print('{} x {:2} = {}' .format(n, 3, n*3))
print('{} x {:2} = {}' .format(n, 4, n*4))
print('{} x {:2} = {}' .format(n, 5, n*5))
print('{} x {:2} = {}' .format(n, 6, n*6))
print('{} x {:2} = {}' .format(n, 7, n*7))
print('{} x {:2} = {}' .format(n, 8, n*8))
print('{} x {:2} = {}' .format(n, 9, n*9))
print('{} x {:2} = {}' .format(n, 10, n*10))


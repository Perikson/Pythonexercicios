n = int(input('Digite um Número: '))
dobro = n*2
triplo = n*3
rq = n**(1/2) #pow(n, 1/)
print('Número inteiro {}, Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.' .format(n, dobro, triplo, rq))

#Pode ser escrito com apenas uma variável:

n = int(input('Digite um número: '))
print('Número: {}, seu dobro é {}, seu triplo é {} e sua raiz quadrarda é {:.2f}.' .format(n, (n*2), (n*3), (n**(1/2))))


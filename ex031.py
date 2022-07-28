d = float(input('Qual a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km' .format(d))
if d <= 200:
    print('O valor a ser pago é de R$ {:.2f}' .format(d * 0.50))
else:
    print('O valor a ser pago é de R$ {:.2f}' .format(d * 0.45))

#Fazendo de maneira simplificada:

d = float(input('Qual a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km' .format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
print('O preço da sua passagem será de R$ {:.2f}' .format(preço))


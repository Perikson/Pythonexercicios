v = float(input('Qual a velocidade atual do carro? '))
m = (v - 80) * 7
if v <= 80:
    print('Tenha um bom dia! Diriga com segurança!')
else:
    print('''Multado!!! Você excedeu o limite permitido que é de 80km/h
Você deve pagar uma multa de R${:.2f}!
Tenha um bom dia! Diriga com Segurança!''' .format(m))

#Usando apenas estrutura simples:

v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    m = (v - 80) * 7
    print('Multado! Você excedeu o limite de velocidade em {:.2f} km/h.' .format(v - 80))
    print('Você deve pagar uma multa no valor de R$ {:.2f}' .format(m))
print('Tenha um bom dia! Diriga com segurança!')

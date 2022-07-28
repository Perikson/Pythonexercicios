p = float(input('Qual é o seu peso? '))
a = float(input('Qual é a sua altura? '))
imc = p / (a * a)

print('O imc dessa pessoa é {:.1f}' .format(imc))

if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc <= 25:
    print('Parabéns, você está na faixa de Peso Normal.')
elif imc <= 30:
    print('Você está com Sobrepeso.')
elif imc <= 40:
    print('Você está em Obesidade.')
else:
    print('CUIDADO, Você está em OBESIDADE MÓRBIDA.')
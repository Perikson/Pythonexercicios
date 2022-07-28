s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while s not in 'MF':
    s = str(input('Dádos inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('Sexo {} registado com sucesso.' .format(s))
from datetime import date

a = int(input('Informe seu ano de nascimento: '))
aa = date.today().year
i = aa - a
print('Ano de nascimento: {}' .format(a))
if i < 18:
    b = 18 - (aa - a)
    print('Quem nasceu em {} tem {} em {}. Ainda faltam {} ano(s) para o alistamento.' .format(a, i, aa, b))
    print('Seu alistamento será em {}.' .format(aa + b))
elif i > 18:
    c = (aa - a) - 18
    print('Quem nasceu em {}, tem {} anos em {}.Você já deveria ter se alistado há {} ano(s).' .format(a, i, aa, c))
    print('Seu alistamento foi em {}.' .format(aa - c))
elif i == 18:
    print('Quem nasceu em {} e tem 18 anos em {}.' .format(a, aa))
    print('Você deve se alistar IMEDIATAMENTE.')
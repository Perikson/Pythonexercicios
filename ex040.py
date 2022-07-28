n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('-=' * 20)
print('Primeira nota = {:.1f}' .format(n1))
print('Segunda nota = {:.1f}' .format(n2))
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}' .format(n1, n2, m))
print('-=' * 20)

if m < 5:
    print('O aluno está REPROVADO.')
elif 5 <= m < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
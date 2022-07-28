exp = str(input('Digite a Expressão: '))
lst = []

for letra in exp:
    if letra == '(':
        lst.append('(')
    elif letra == ')':
        if len(lst) > 0:
            lst.pop()
        else:
            lst.append(')')
            break

if len(lst) == 0:
    print('Expressão Válida.')
else:
    print('Expressão Inválida.')
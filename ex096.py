def área(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a:.2f}m².')


l = float(input('Largura do Terreno: '))
c = float(input('Comprimento do Terreno: '))
área(l, c)
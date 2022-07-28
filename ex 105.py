def notas(* n):
    dicio = {}
    max = tot = som = 0
    min = 10
    for v in n:
        if v > max:
            max = v
        if v < min:
            min = v
        tot += 1
        som += v
    dicio['Total de Notas'] = tot
    dicio['Maior'] = max
    dicio['Menor'] = min
    dicio['Média'] = som / tot
    return dicio


print(notas(5, 8, 9))

#TAMBÉM PODE SER ESCRITO ASSIM:

def notas2(* n):
    dicio = dict()
    dicio['Total de Notas'] = len(n)
    dicio['Maior'] = max(n)
    dicio['Menor'] = min(n)
    dicio['Média'] = sum(n) / len(n)
    return dicio


print(notas2(4, 8, 10))
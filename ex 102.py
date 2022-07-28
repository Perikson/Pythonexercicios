def fatorial(n, show = False):
    f = 1
    for v in range(n, 0, -1):
        f *= v
        if show:
            if v > 1:
                print(f'{v} x ', end='')
            else:
                print(f'{v} = ', end='')
    return f


print(fatorial(5, show = True))
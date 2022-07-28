lp = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
      'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')


for l in lp:
      print(f'\nNa palavra {l.upper()} temos as vogais: ', end='')
      for v in l:
            if v in 'aeiou':
                  print(f'{v:^2}', end='')

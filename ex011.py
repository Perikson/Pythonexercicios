lp = float(input('Digite a largura da parede: '))
ap = float(input('Digite a Altura da parede: '))
print('Largura da parede: {} \nAltura da parede: {}m²'.format(lp, ap))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}.' .format(lp, ap, (lp*ap)))
print('Parra pintar essa parede, você precisará de {}l de tinta.' .format((lp*ap)/2))
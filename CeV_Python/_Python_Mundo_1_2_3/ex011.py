largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura 

litro_tinta = area / 2

print(f'A área dessa parede é de {area:.1f}m².')
print(f'Serão necessários {litro_tinta:.1f}l de tinta para pintar essa parede')
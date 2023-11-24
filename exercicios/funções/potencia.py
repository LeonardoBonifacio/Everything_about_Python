def potencia(base,expoente):
    exponenciacao = base ** expoente
    print(f'O resulta de {base}^{expoente} é {exponenciacao}')


print('Digite uma base e um expoente para calcula uma exponenciação: ')
potencia(int(input('Base: ')),int(input('Expoente: ')))

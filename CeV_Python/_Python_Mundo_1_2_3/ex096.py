from os import system
system('cls')

def area(largura,comprimento):
    print('CONTROLE DE TERRENOS')
    print('---------------------')
    area = largura * comprimento
    print(f'A área do terreno com {largura}x{comprimento} é de {area}m²')



larg = float(input('LARGURA (m): '))
compri = float(input('COMPRIMENTO (m): '))
area(larg,compri)

'''
Um empreendimento de carga e descarga de trens alterou a modalidade de trabalho para atender a demanda de exportação dos produtos que agora são organizados em containers gerenciados por QR-CODE. Antes o sistema gerenciava o destina da carga pela cor do container. Para esse mudança ocorrer, ainda há a necessidade de alteração no equipamento das pessoas que trabalham na empresa, entretanto esse processo é demorado e custoso. Desta forma, visando acelerar o processo, foi inserido junto ao QR-CODE um sistema de pontos que informa o destino do container. Você apresentou a ideia de usar o celular como leitor, visando reduzir os custo e ficou encarregado de indentificar o destino do carregamento. Seu papel é desenvolver um sistema que encaminhe conforme a estrutura abaixo:

1 e 1 == Portugal
1 e 2 == Espanha
2 e 1 == Argentina
2 e 2 == Paraguai
3 e 1 == Namíbia
3 e 2 == Zâmbia
3 e 3 == Zimbabwe
'''

from os import system
system('cls')

print('-=-=-=-=-=-=-=-ENCAMINHANDO CARGAS-=-=-=-=-=-=-=-')

print('Por favor , utilize nosso sistema de pontos em colunas para encaminhar sua carga.')

coluna_continente = int(input('[1 ponto] - Europa\n[2 pontos] - América do sul\n[3 pontos] - Africa\n-> '))
if(coluna_continente == 1):
    coluna_pais = int(input('Vai para a Europa, escolha o pais por favor.\n[1 ponto] - Portugal\n[2 pontos] - Espanha\n-> '))
    if(coluna_pais == 1):
        print('Destino Portugal.')
    elif(coluna_pais == 2):
        print('Destino Espanha')
    else:
        print('Valor inválido.')
elif(coluna_continente == 2):
    coluna_pais = int(input('Vai para a América do Sul, escolha o país por favor.\n[1 ponto] - Argentina\n[2 pontos] - Paraguai\n->  '))
    if(coluna_pais == 1):
        print('Destino Argentina')
    elif(coluna_pais):
        print('Destino Paraguai')
    else:
        print('Valor inválido')
elif(coluna_continente == 3):
    coluna_pais = int(input('Vai para a África, escolha o páis por favor.\n[1 ponto] - Namíbia\n[2 pontos] - Zâmbia\n[3 pontos] - Zimbabwe\n-> '))
    if(coluna_pais == 1):
        print('Destino Namíbia')
    elif(coluna_pais == 2):
        print('Destino Zâmbia')
    elif(coluna_pais == 3):
        print('Destino Zimbabwe')
    else:
        print('Valor inválido')
else:
    print('Você digitou um valor inválido para continente.')
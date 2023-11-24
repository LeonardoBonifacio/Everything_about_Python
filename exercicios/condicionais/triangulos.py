from os import system
system('cls')

print('----------É TRIÂNGULO?----------')

segmento1 = float(input('Digite o tamanho do primeiro segmento de reta: '))
segmento2 = float(input('Digite o tamanho do segundo segmento de reta: '))
segmento3 = float(input('Digite o tamanho do terceiro segmento de reta: '))


if(segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2):
    print('Com esses segmentos de reta podem ser formados um triângulo')
    if(segmento1 == segmento2 and segmento2 == segmento3):
        print('Tipo de triângulo: EQUILÁTERO')
    elif(segmento1 == segmento2 or segmento2 == segmento3 or segmento1 == segmento3):
        print('Tipo de triângulo: ISÓSCELES')
    else:
        print('Tipo de triângulo: ESCALENO')
else:
    print('Com esses segmentos de reta não podemos formar um triângulo')
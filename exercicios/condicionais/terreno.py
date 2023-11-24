from os import system
system('cls')

print('__________TIPO DE TERRENO__________')

largura = float(input('Digite qual é a largura do terreno: '))
comprimento = float(input('Digite qual é o comprimento do terreno: '))
area = largura * comprimento

print(f'A área de seu terreno é de {area:.2f}m² .')

if(area < 100.0):
    print('Abaixo de 100m² = TERRENO POPULAR')
elif(area > 100.00 and area <= 500.00):
    print('Entre 100m² e 500m² = TERRENO MASTER')
else:
    print('Acima de 500m² = TERRENO VIP')
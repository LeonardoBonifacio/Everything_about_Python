from os import system
system('cls')

peso_frutas = float(input('Digite o peso em Kg de frutas compradas: '))
if(peso_frutas < 0):
    print('Valor inválido')
elif(peso_frutas == 0):
    print('Você não comprou frutas .')
elif(peso_frutas <= 3.0):
    print('Você pagará R$3,00/Kg')
elif(peso_frutas <= 5.0):
    print('Você pagará R$2,75/kg')
elif(peso_frutas <= 10):
    print('Você pagará R$2,50/kg')
else:
    print('Você pagará R$2,25/kg')
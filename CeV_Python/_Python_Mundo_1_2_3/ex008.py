from os import system
system('cls')

print('=====CONVERTENDO MEDIDAS=====')
metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
kilometro = metros / 1000
hectometros = metros / 100
decametros = metros / 10
decimetros = metros * 10


print(f'O valor {metros:.2f}m  corresponde a:  \n {kilometro:.3f}km \n {hectometros:.2f}hm \n {decametros:.2f}dam \n {decimetros:.2f}dm \n {centimetros:.2f}cm \n {milimetros:.2f}mm \n PROGRAMA FINALIZADO COM SUCESSO')

'''
km hm dam m dm cm mm
'''
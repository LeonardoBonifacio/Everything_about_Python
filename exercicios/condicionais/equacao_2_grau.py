from os import system
from math import sqrt
system('cls')
#Equação do 2 grau 

print('-=-' * 10, 'EQUAÇÃO DO 2° GRAU', '-=-' * 10 )

a = int(input('Digite o valor de A: '))
if(a == 0):
    prinnt('Estamos calculando uma equação do 2° grau , logo o valor de A não pode ser 0')
else:    
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
delta = (b ** 2) - (4 * a * c)
baskhara_positivo =  (- b + (delta ** (1 / 2))) / (2 * a)
baskhara_negativo = (- b - (delta ** (1 / 2)))/ (2 * a)
if(delta < 0):
    print(f'O valor de delta foi negativo -- > {delta}, logo essa equação não possui raizes reais.')
elif(delta == 0):
    print(f'O valor de delta foi igual a 0 , logo essa equação possui apenas uma raiz real que é {-b / 2 * a}')
elif(delta > 0):
    print(f'O valor de delta foi positivo, logo essa equação possui duas raizes reais que são {baskhara_positivo:.2f} e {baskhara_negativo:.2f}')
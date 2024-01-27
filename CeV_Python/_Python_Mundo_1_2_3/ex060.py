from os import system
system('cls')

fatorial = int(input('Número que deseja saber fatorial >>> '))
primeiro = fatorial
cont = fatorial - 1
string_fatorial = str(fatorial)
while(cont > 0):
    fatorial *= cont
    string_fatorial += ' ' + str(cont)
    cont -= 1
print(f'O fatorial de {primeiro}! é {string_fatorial.replace(" ", " x ")} = {fatorial}')

'''
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')
'''

'''
num = int(input('Digite um número para calcular seu Fatorial: '))
cont = num
fatorial = 1
print(f'Calculando {n}!',end = '')
while(cont > 0):
    print(cont,end = '')
    print(' x ' if cont > 1 else ' = ',end = '')
    fatorial *= cont
    cont -= 1
print(f)
'''
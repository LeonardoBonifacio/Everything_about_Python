#Programa que lê um número entre 0 e 9999 e mostra na tela cada um dos digitos separados
from os import system
system('cls')


num = int(input('Digite um número entre 0 e 9999: '))

unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhares = num // 1000 % 10

if(num < 0 or num > 9999):
    print('Você não digitou um valor válido.')
else:
    print(f'Milhares: {milhares}')
    print(f'Centenas: {centenas}')
    print(f'Dezenas: {dezenas}')
    print(f'Unidades: {unidades}')









#Jeito feito pela formatação de strings
'''num = str((input('Digite um número entre 0 e 9999: ')))

if(int(num) < 0 or int(num) > 9999):
    print('Você não digitou um número válido.')
else:
    print(f'Unidades: {num[3]}')
    print(f'Dezenas: {num[2]}')
    print(f'Centenas: {num[1]}')
    print(f'Milhares: {num[0]}')'''
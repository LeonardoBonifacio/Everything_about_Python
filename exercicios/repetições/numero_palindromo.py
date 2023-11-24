'''
Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501 
'''
from os import system
system('cls')

print('-=-' * 10,'VERIFICANDO SE UM NÚMERO É PALÍNDROMO','-=-' * 10)

num = str(input('Número inteiro a verificar: '))
num_invertido = num[::-1]
if(num_invertido == num):
    print(f'O número {num} ao contrário é {num_invertido} ou seja é palíndromo')
else:
    print(f'O número {num} ao contrário é {num_invertido} ou seja ele não é um palíndromo.')
'''
Programa que armazena o nome do usuario e lhe apresenta uma
CALCULADORA DAS OPERAÇÕES DA MATEMÁTICA
'''
import os
os.system('cls')

us_name = input('Digite seu nome: ')
print(f'Olá,{us_name}. Adiante use a calculadora que inclui algumas  das operações da matemática.')

print('-----CALCULADORA-----')

numA = int(input('Digite um número: '))
numB = int(input('Digite outro número: '))

print(f'Soma de {numA} + {numB} = {numA + numB} ')

print(f'Subtração de {numA} - {numB} = {numA -numB}')

print(f'Multiplicação de {numA} * {numB} = {numA * numB}')

print(f'Divisão de {numA} / {numB} = {numA / numB}')

print(f'Potenciação de {numA} ^ {numB} = {numA ** numB}')

print(f'Divisão inteira de {numA} // {numB} = {numA // numB}') 

print(f'O resto da divisão de {numA} % {numB} = {numA % numB}')
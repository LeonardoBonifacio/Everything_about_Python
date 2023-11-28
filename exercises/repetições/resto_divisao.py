"""
Escreva um programa que calcule o resto da divisão inteira entre
dois números. Utilize apenas as operações de soma e subtração para calcular o resultado. 
"""
from os import system
system('cls')

print('-=-' * 10,'CALCULANDO RESTO DA DIVISÃO','-=-' * 10)

num1 = int(input('1° número: '))
num2 = int(input('2° número: '))

divisor = num1
dividendo = num2
qtd_divisoes = 0

while(divisor >= dividendo):
    divisor -= dividendo
    qtd_divisoes += 1
resto =  num1 - (qtd_divisoes * num2)
print(f'O resto da divisão inteira entre {num1} e {num2} é {resto}')


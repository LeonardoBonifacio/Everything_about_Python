"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
from os import system
system('cls')
print('-=-' * 10,'NÚMEROS QUE ESTÃO ENTRE ESSES NÚMEROS','-=-' * 10)
num1 = int(input('1° número: '))
num2 = int(input('2° número: '))
if(num1 < num2):
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1
soma = 0
for nums in range(menor + 1,maior,1):
    print(f'[{nums}]',end = ' ')
    soma += nums
print(f'--> A soma desses números é {soma}.')
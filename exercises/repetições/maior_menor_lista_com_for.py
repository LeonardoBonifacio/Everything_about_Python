from os import system
system('cls')
from math import inf
'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.''' 
soma = 0
lista_num = []
maior = - inf
menor = inf

n = float(input('Quer digitar quantos números: '))
for numeros in range(int(n)):
    while(True):
        num = int(input(f'{numeros + 1}° Número: '))
        if(num > 0 and num < 1000):
            lista_num.append(num)
            break
        print('Você precisa digitar um número maior que 0 e menor que 1000')
for numeros in (lista_num):
    if(numeros > maior):
        maior = numeros
    if(numeros < menor):
        menor = numeros
    soma += numeros
print(f'O maior número dessa lista {lista_num} digitados é {maior}\nO menor número é {menor} e a soma de todos é {soma}')

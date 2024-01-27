from os import system
system('cls')
from random import randint
print('-=-' * 10,'SORTEANDO NÚMEROS EM TUPLAS','-=-' * 10)
tupla_de_nums = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os números gerados foram: ',end = '')
for num in tupla_de_nums:
    print(num,end = ' ')
print(f'\nNúmeros em ordem crescente: ',end = '')
for num in sorted(tupla_de_nums):
    print(num,end = ' ')
'''maior = -1
menor = 11
for num in tupla_de_nums:
    if(num > maior):
        maior = num
    if(num < menor):
        menor = num'''
print(f'\nO menor número dessa tupla foi {min(tupla_de_nums)}\nEnquanto o maior número foi {max(tupla_de_nums)}')

#Também poderia usar os métodos max e min das coleções do python para descobrir o menor e o maior valor sorteado dentro dessa tupla:
#print(f'O maior valor sorteado foi {max(tupla_de_nums)}.')
#print(f'O menor valor sorteado foi {min(tupla_de_nums)}.')

#ou faço do jeito classico de testar um por um item com repetições
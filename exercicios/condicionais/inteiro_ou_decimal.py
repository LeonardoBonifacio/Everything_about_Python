from os import system
from math import ceil
system('cls')

num = float(input('Digite qualquer número: '))

if(ceil(num) > num):
    print(f'O número {num} é decimal')
else:
    print(f'O número {num} é inteiro')
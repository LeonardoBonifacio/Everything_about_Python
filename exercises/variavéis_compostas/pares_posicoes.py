from os import system
system('cls')

inteiros = []

for inteiro in range(10):
    inteiros.append(int(input(f'Digite o {inteiro + 1}° númeor inteiro: ')))
for pos,inteiro in enumerate(inteiros):
    if(inteiro % 2 == 0):
        print(f'O número {inteiro} é par e ele estava armazenada na posição {pos + 1} dessa lista')
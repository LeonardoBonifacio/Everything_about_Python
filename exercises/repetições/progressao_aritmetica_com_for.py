from os import system
system('cls')

print('PROGRESSÃO ARITMÉTICA')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão:  '))
soma = 0
for termos in range(primeiro_termo,primeiro_termo + (11 - 1) * razao,razao):
    print(termos, end = ' ')
    soma += termos
print(f'\nA soma desses 10 termos é {soma}.')
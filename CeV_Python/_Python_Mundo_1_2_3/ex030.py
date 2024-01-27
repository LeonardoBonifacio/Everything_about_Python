from os import system
system('cls')

print('__________É PAR OU IMPAR?__________')

num = int(input('Digite um número inteiro qualquer: '))

if(num % 2 == 0 ):
    print(f'{num} É PAR.')
else:
    print(f'{num} É IMPAR.')

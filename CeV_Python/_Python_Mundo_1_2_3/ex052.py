from os import system
system('cls')

print('-=-' * 10, 'VERIFICADOR DE NÚMEROS PRIMOS' , '-=-' * 10)
lista_divisores = []
divisores = 0
num = int(input('Digite um número inteiro qualquer: '))
for i in range(1,num + 1):
    if(num % i == 0):
        divisores += 1
        print(f'\033[32m{i}\033[m',end = ' ')
        lista_divisores.append(i)
    else:
        print(f'\033[31m{i}\033[m',end = ' ')
if(divisores == 2):
    print(f'\nO número {num} é Primo')
    print(f'Pois foi divisivel somente por \033[1m{lista_divisores}\033[m')
else:
    print(f'\nO número {num} não é Primo')
    print(f'Pois foi divisivel pelo números \033[1m{lista_divisores}\033[m')
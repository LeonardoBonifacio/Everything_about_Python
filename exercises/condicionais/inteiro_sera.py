from os import system
system('cls')

num_int = int(input('Digite um número inteiro qualquer: '))

if(num_int > 0):
    print(f'O número {num_int} é positivo.')
elif(num_int < 0):
    print(f'O número {num_int} é negativo.')
else:
    print(f'O número {num_int} é igual a 0.')
from os import system
system('cls')

num = int(input('Digite um número inteiro: '))
antecessor = num
print(f'Número inicial: {num}')
print(f'Somando {num} com seus 10 antecessores.')
for i in range(10):
    antecessor = antecessor - 1
    print(f'A soma de {num} + {antecessor} = {num + antecessor}')
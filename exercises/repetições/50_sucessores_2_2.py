from os import system
system('cls')

num = int(input('Digite um número inteiro para saber os seus 50 sucessores de 2 em 2 : '))
print(num)
for i in range(50):
    num = num + 2
    print(num)
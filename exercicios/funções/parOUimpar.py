from os import system
system('cls')


def parOuimpar(num):
    if(num == ''):
        print('Nenhum número foi digitado')
    elif(num == '0' ):
        print('0 não é nem par e nem impar')
    elif(int(num) % 2 == 0):
        print(f'{num} é par')
    else:
        print(f'{num} é impar')


parOuimpar(input('Digite um número inteiro para verificar se é par ou impar: '))
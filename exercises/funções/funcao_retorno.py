from os import system
system('cls')

def retonaDobro(numero):
    dobro  = numero * 2
    return dobro
num = int(input('Digite um valor para saber o dobro do mesmo: '))
print(f'O dobro de {num} é {retonaDobro(num)}')
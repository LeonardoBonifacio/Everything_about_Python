from os import system
system('cls')

contador = 0

num = int(input('Digite qualquer número inteiro e eu lhe mostrarei os seus cinquenta sucessores: '))

while(contador != 51):
    contador = contador + 1
    print(num)
    num = num + 1
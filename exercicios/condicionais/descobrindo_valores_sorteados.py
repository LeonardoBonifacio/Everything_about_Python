from os import system
system('cls')

from random import randint

numero_sorteado = randint(1,5)

print('__________TENTE ACERTAR QUE NÚMERO EU ESCOLHI__________')

print('Este jogo consiste em uma advinha de números entre 1 e 5')

numero_escolhido = int(input('Digite que número você acha que eu escolhi: '))

if(numero_escolhido == numero_sorteado):
    print(f'Meus parabens você acertou , eu pensei no número {numero_sorteado} ')
else:
    print(f'Você errou o número que eu escolhi, eu escolhi o número {numero_sorteado}')

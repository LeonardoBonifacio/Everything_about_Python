from os import system
system('cls')
from random import randint

numero_sortado = randint(1, 10)

for tentativas in range(1,5):
    print('Tente sortear um número entre 1 e 10')
    print(f'Tentativa número: {tentativas}°\nVocê tem até 4 tentativas')
    numero_escolhido = int(input(f'Sua {tentativas}° tentativa: '))
    if(numero_escolhido == numero_sortado):
        print('Parabens você acertou')
        break
    else:
        print(f'ERRROU')
        print()
if(numero_escolhido != numero_escolhido):
    print(f'Você perdeu mesmo com 4 tentativas.')
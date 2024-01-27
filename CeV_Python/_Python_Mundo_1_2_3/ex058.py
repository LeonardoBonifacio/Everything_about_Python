from random import randint
from os import system
system('cls')

numero_pensado = randint(0, 10)
numero_escolhido = 15
tentativas = 1
print('-=--=--=--=--=- JOGO DA ADIVINHAÇÃO -=--=--=--=--=-')
print('Acabei de pensar em um número entre 0 e 10\nSerá que você consegue adivinhar qual foi? ')
while(numero_escolhido != numero_pensado):
    numero_escolhido = int(
        input(f'Sua {tentativas}° tentativa:   '))
    if(numero_escolhido > numero_pensado):
        print('Menos... Tente mais uma vez.')
        tentativas += 1
    elif(numero_escolhido < numero_pensado):
        print('Mais... Tente mais uma vez')
        tentativas += 1
print(f'Parabens por acertar em {tentativas} tentativas que eu estava pensando no número --> {numero_pensado}')

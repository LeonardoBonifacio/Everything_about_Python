from random import randint
from time import sleep
from os import system
system('cls')

print('----------ADIVINHE QUE NÚMERO ESTOU PENSANDO----------')

print('Dica: Estou pensansdo em um número entre 0 e 5')
numero_pensado = randint(0,5) # Faz o computador 'pensar' num número entre 0 e 5
numero_escolhido = int(input('Digite que número você acha que estou pensando: '))# Jogador tenta advinhar
print('-=-=-=-=PROCESSANDO-=-=-=-=-')
sleep(3)
if(numero_escolhido == numero_pensado):
    print(f'PARABENS, Você acertou o número que eu estava pensando -> {numero_pensado}')
elif(numero_escolhido < 0 or numero_escolhido > 5):
    print('Você é burro é? Não ta vendo que eu pensei em um número entre 0 e 5.')
else:
    print(f'Você errou,  eu pensei no número -> {numero_pensado} e não no número --> {numero_escolhido}')

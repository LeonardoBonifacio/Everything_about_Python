from os import system
system('cls')
from time import sleep
import random

print('-=-' * 14, 'JOKENPO' , '-=-' * 14)

escolha_jogador = int(input('[ 1 ] - PEDRA\n[ 2 ] - PAPEL\n[ 3 ] - TESOURA\nSua jogada >>>  '))
escolha_computador = random.randint(1,3)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

if(escolha_jogador == 1 and escolha_computador == 1):
    print('JOGADOR escolheu Pedra\nCOMPUTADOR escolheu Pedra')
    print('EMPATE')
elif(escolha_jogador == 1 and escolha_computador == 2):
    print('JOGADOR escolheu Pedra\nCOMPUTADOR escolheu Papel')
    print('GANHEI...')
elif(escolha_jogador == 1 and escolha_computador == 3):
    print('JOGADOR escolheu Pedra\nCOMPUTADOR escolheu Tesoura')
    print('VOCÊ ME DERROTOU...')
elif(escolha_jogador == 2 and escolha_computador == 1):
    print('JOGADOR escolheu Papel\nCOMPUTADOR escolheu Pedra')
    print('VOCÊ ME DERROTOU...')
elif(escolha_jogador == 2 and escolha_computador == 2):
    print('JOGADOR escolheu Papel\nCOMPUTADOR escolheu Papel')
    print('EMPATE')
elif(escolha_jogador == 2 and escolha_computador == 3):
    print('JOGADOR escolheu Papel\nCOMPUTADOR escolheu Tesoura')
    print('GANHEI...')
elif(escolha_jogador == 3 and escolha_computador == 1):
    print('JOGADOR escolheu Tesoura\nCOMPUTADOR escolheu Pedra')
    print('GANHEI')
elif(escolha_jogador == 3 and escolha_computador == 2):
    print('JOGADOR escolheu Tesoura\nCOMPUTADOR escolheu Papel')
    print('VOCÊ ME DERROTOU...')
elif(escolha_jogador == 3 and escolha_computador == 3):
    print('JOGADOR escolheu Tesoura\nCOMPUTADOR escolheu Tesoura')
    print('EMPATE')
else:
    print('Opção inválida.')
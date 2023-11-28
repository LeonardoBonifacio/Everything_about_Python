from os import system
system('cls')

from random import randint

aleatorio_pedra_papel_tesoura = randint(1,3)

'''
Valores aletorios de 1 a 3
1 == Pedra
2 == Papel
3 == Tesoura
'''

print('__________JoKenPo Justo__________')

pedra_papel_tesoura = int(input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n-> '))

if(pedra_papel_tesoura == 1 and aleatorio_pedra_papel_tesoura == 1):
    print('Empate, pois, também escolhi Pedra.')
elif(pedra_papel_tesoura == 1 and aleatorio_pedra_papel_tesoura == 2):
    print('Eu ganhei , pois escolhi papel e você escolheu pedra')
elif(pedra_papel_tesoura == 1 and aleatorio_pedra_papel_tesoura == 3):
    print('Você ganhou, pois eu escolhi Tesoura e você pedra')
elif(pedra_papel_tesoura == 2 and aleatorio_pedra_papel_tesoura == 1):
    print('Você ganhou, pois eu escolhi pedra e você papel')
elif(pedra_papel_tesoura == 2 and aleatorio_pedra_papel_tesoura == 2):
    print('Empate, pois, também escolhi papel.')
elif(pedra_papel_tesoura == 2 and aleatorio_pedra_papel_tesoura == 3):
    print('Eu ganhei, pois, eu escolhi tesoura e você papel.')
elif(pedra_papel_tesoura == 3 and aleatorio_pedra_papel_tesoura == 1):
    print('Eu ganhei, pois, eu escolhi pedra e você tesoura')
elif(pedra_papel_tesoura == 3 and aleatorio_pedra_papel_tesoura ==2):
    print('Você ganhou, pois, eu escolhi Papel e você Tesoura')
elif(pedra_papel_tesoura == 3 and aleatorio_pedra_papel_tesoura == 3):
    print('Empate, pois, também escolhi tesoura')
else:
    print('Você não escolheu uma opção válida.')


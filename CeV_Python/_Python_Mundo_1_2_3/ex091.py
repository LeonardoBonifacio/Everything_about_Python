from os import system
system('cls')
from random import randint
from time import sleep

#Como ordenar um dicionario/Meu jeito e do Guanabara


jogadores = {'jogador1': randint(1,6),
             'jogador2': randint(1,6), 
             'jogador3': randint(1,6),
             'jogador4': randint(1,6)
              }

print('Valores sorteados:')

for k,v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('  == Ranking dos jogadores ==  ')
c = 1
for i in sorted(jogadores, key = jogadores.get, reverse = True):
    print(f'    {c}° lugar: {i} com {jogadores[i]}')
    sleep(1)
    c += 1

"""
#Jeito do guanabara

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)
        }
ranking = list()

print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(),key = itemgetter(1), reverse = True)
print('-=-' * 30)
print('  == RANKING DOS JOGADORES ==  ' )
for i,v in enumerate(ranking):
    print(f'    {i +  1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
"""
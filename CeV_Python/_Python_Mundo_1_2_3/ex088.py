from os import system
system('cls')
from random import randint
from time import sleep
print('=' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('=' * 30)

jogos = []

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for jogo in range(qtd_jogos):
    jogos.append([])
for jogo in (jogos):
    while(len(jogo) < 6):
        num = randint(1,60)
        if(len(jogo) == 0):
            jogo.append(num)
        else:
            if(num not in jogo):
                jogo.append(num)
print(f'-=-=-=-=-=- SORTEANDO {qtd_jogos} JOGOS -=-=-=-=-=-')
for pos,jogo in enumerate(jogos):
    print(f'Jogo {pos + 1}: {sorted(jogo)}')
    sleep(1)
print('-=-=-=-=-=- BOA SORTE -=-=-=-=-=-')

#Solução do guanabara

'''
from time import sleep
from random import randint

lista = list()
jogos = list()
print('-=' * 30)
print('       JOGA NA MEGA SENA        ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while(tot <= quant):
    cont = 0
    while(True):
        num = randint(1,60)
        if(num not in lista):
            lista.append(num)
            cont += 1
        if(cont >= 6):
            break
    lista.sort()
    jogos.append(lista.copy())
    lista.clear()
    tot += 1
print('-=' * 3,f'SORTEANDO {quant} JOGOS ', '-=' * 3) 
for i,l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5,'< BOA SORTE >','-=' * 5)
            
'''
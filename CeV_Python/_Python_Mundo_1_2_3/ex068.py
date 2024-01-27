from os import system
system('cls')
from random import randint
soma = qtd_vitorias = 0
while(True):
    print('VAMOS JOGAR PAR OU IMPAR')
    while(True):
        num_jog = int(input('Escolha seu número[ENTRE 0 e 10]:  '))
        if(num_jog <= 10 and num_jog >= 0):
            break
        else:
            print('Número inválido...')
    num_comput = randint(0,10)
    soma = num_comput + num_jog
    while(True):
        escolha_par_ou_impar = str(input('[P]ar ou [I]mpar: ')).strip().upper()[0]
        if(escolha_par_ou_impar == 'P' or escolha_par_ou_impar == 'I'):
            break
        else:
            print('Valor inválido para [P]ar ou[I]mpar')
    if(soma % 2 == 0):#PAR
        if(escolha_par_ou_impar == 'P'):#PAR
            qtd_vitorias += 1
            print('\033[1mVocê GANHOU\033[m')
            print('-=-' * 20)
            print(f'Você jogou {num_jog} e eu joguei {num_comput} totalizando {soma} ou seja PAR')
            print('-=-' * 20)
        else:#IMPAR
            print('\033[1mVocê PERDEU\033[m')
            print('-=-' * 20)
            print(f'Você jogou {num_jog} e eu joguei {num_comput} totalizando {soma} ou seja PAR')
            print('-=-' * 20)
            print('\033[1mQue perdedor ein...\033[m')
            break
    else:#IMPAR
        if(escolha_par_ou_impar == 'P'):#PAR
            print('\033[1mVocê PERDEU\033[m')
            print('-=-' * 20)
            print(f'Você jogou {num_jog} e eu joguei {num_comput} totalizando {soma} ou seja IMPAR')
            print('-=-' * 20)
            print('\033[1mQue perdedor ein...\033[m')
            break
        else:#IMPAR
            qtd_vitorias += 1
            print('\033[1mVocê GANHOU\033[m')
            print('-=-' * 20)
            print(f'Você jogou {num_jog} e eu {num_comput} totalizando {soma} ou seja IMPAR')
            print('-=-' * 20)
        input('\033[1mVamos jogar novamente,pressione [ENTER]...\033[m')
        system('cls')

print(f'GAME OVER,você venceu apenas {qtd_vitorias}')


"""
Codigo do guanabara

from random import randint
v = 0
while(True):
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador 
    tipo = ' '
    while(tipo not in 'PI'):
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}.Total de {total} ',end = '')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if(tipo == 'P'):
        if(total % 2 == 0):
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif(tipo == 'I'):
        if(total % 2 == 1):
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print('GAME OVER! Você venceu {v} vezes.')
"""


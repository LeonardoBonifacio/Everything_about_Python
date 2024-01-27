from os import system
system('cls')
from time import sleep

def PyHELP():
    while(True):
        print('~'* 30)
        print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
        print('~'* 30)
        funcao_ou_lib = str(input('Função ou Biblioteca > '))
        if(funcao_ou_lib.upper() == 'FIM'):
            break
        else:
            print('~' * 30)
            print(f"{'ACESSANDO O MANUAL DO COMANDO/LIB':^30}",f'{funcao_ou_lib}')
            sleep(1)
            help(funcao_ou_lib)
PyHELP()
print(f'{"ATÉ LOGO":^30}')
print('~' * 30)

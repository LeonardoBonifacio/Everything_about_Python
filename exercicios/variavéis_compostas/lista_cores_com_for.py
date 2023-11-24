from os import system
system('cls')

lista_de_cores = ['Azul', 'Branco', 'Cinza', 'Vermelho']

for cor in lista_de_cores:
    if(cor == 'Azul'):
        print(f'\033[34m{cor}\033[m')
    if(cor == 'Branco'):
        print(f'\033[37m{cor}\033[m')
    if(cor == 'Cinza'):
        print(f'\033[30m{cor}\033[m')
    if(cor == 'Vermelho'):
        print(f'\033[31m{cor}\033[m')
from os import system
system('cls')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
n_termos = primeiro_termo + (10 - 1) * razao
qtd_termos = 10
qtd = 1
print(primeiro_termo,end = ' - ')
while(primeiro_termo < n_termos):
    primeiro_termo += razao
    print(primeiro_termo,end = ' - ')
    if(primeiro_termo == n_termos):
        print('Pausa')
        while(qtd != 0):
            qtd = int(input('\nDeseja mostrar mais quantos termos? '))
            qtd_termos += qtd
            if(qtd != 0):
                primeiro_termo += razao
                n_termos = primeiro_termo  + (qtd - 1) * razao
                system('cls')
                print(primeiro_termo,end = ' - ')
                while(primeiro_termo < n_termos):
                    primeiro_termo += razao
                    print(primeiro_termo,end = ' - ')
                print('Pausa')
print('-CABOU-')
print(f'Foram mostrados {qtd_termos} termos.')

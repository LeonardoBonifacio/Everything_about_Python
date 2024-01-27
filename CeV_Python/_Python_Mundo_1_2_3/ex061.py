from os import system
system('cls')

print('-=--=--=- PROGRESSÃO ARITMÉTICA -=--=--=-')

primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão de uma PA: '))
n_termo = primeiro_termo + (10 - 1) * razao
print(primeiro_termo,end = ' - ')
while(primeiro_termo < n_termo):
    primeiro_termo += razao
    print(primeiro_termo,end =' - ')
print('Cabou')
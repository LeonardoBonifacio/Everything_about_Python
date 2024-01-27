from os import system
system('cls')
from time import sleep

def contador(inicio, fim, passo):
    print('-=' * 20)
    if(passo < 0):
        passo *= -1
    if(passo == 0):
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if(inicio < fim):
        cont = inicio
        while(cont <= fim):
            print(f'{cont}',end=' ',flush=True)
            sleep(0.1)
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while(cont >= fim):
            print(f'{cont}',end=' ',flush=True)
            sleep(0.1)
            cont -= passo
        print('Fim!')
    print('-=' * 20)
    print()


contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem...')


inic = int(input('Digite o valor inicial da contagem: '))
fim = int(input('Digite o valor final da contagem: '))
pas = int(input('Digite de quanto em quanto você quer contar: '))

    

contador(inic,fim,pas)

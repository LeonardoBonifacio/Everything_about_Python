from os import system
system('cls')
from time import sleep

def maior(*lista):
    print('-=' * 30)
    if(len(lista) > 0):
        maior = max(lista)
        print('Analisando os valores passados...')
        for valor in lista:
            print(valor,end = ' ',flush=True)
            sleep(0.2)
        print(f'Foram informados {len(lista)} valores')
        print(f'O maior valor informado foi {maior}')
    else:
        print('Analisando os valores passados')
        print('Foram informados 0 valores ao todo')
        print('O maior valor informado foi 0.')
    print('-=' * 30)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()





from os import system
system('cls')
from random import randint
from time import sleep
def sorteadora():
    lista = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]
    print('Sorteando cinco valores da lista:',end= ' ')
    for num in lista:
        print(num,end= ' ',flush=True)
        sleep(0.4)
    print('PRONTO!')
    return lista
valores = sorteadora()
def soma_par(lista_valores):
    pares = 0
    for valor in valores:
        if(valor % 2 == 0):
            pares += valor
    print(f'Somando os valores pares de {valores}, temos {pares}')
soma_par(valores)


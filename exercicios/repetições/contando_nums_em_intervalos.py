'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].

A entrada de dados deverá terminar quando for lido um número negativo.'''
from os import system
system('cls')

print('-=-' * 10,'CONTANDO NÚMEROS EM INTERVALOS','-=-' * 10)
cont_entre_0_25 = cont_entre_25_50 = cont_entre_50_75 = cont_entre_75_100 = qtd_num = 0
while(True):
    num = int(input('Digite um número inteiro positivo ou um número negativo to stop: '))
    if(num < 0):
        break
    elif(num > 0 and num <= 25):
        cont_entre_0_25 += 1
    elif(num > 25 and num <= 50):
        cont_entre_25_50 += 1
    elif(num > 50 and num <= 75):
        cont_entre_50_75 += 1
    elif(num > 75 and num <= 100):
        cont_entre_75_100 += 1
    qtd_num += 1
print(f'Dos {qtd_num} números digitados:\n{cont_entre_0_25} estavam entre 0 e 25\n{cont_entre_25_50} estavam entre 25 e 50\n{cont_entre_50_75} estavam entre 50 e 75\n{cont_entre_75_100} estavam entre 75 e 100')
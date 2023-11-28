'''
João papo-de-pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo(50kg) deve pagar uma multa de R$ 4,00 por kilo excedente. João precisa que você faça um programa que leia a variável peso(peso de peixes) e calcule o exceso. Gravar na varável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

import os
os.system('cls')

regulamento = 50
multa_fixa = 4

peso_peixes = int(input('Digite o peso dos  peixes:  '))

if(peso_peixes > 50):
    excesso = peso_peixes - regulamento
    multa_a_pagar = excesso * multa_fixa
    print(f'Como você ultrapassou o peso em kg de peixes dado pelo regulament({regulamento}kg), e o valor da multa sendo {multa_fixa}R$ por kilo excedente de peixes o valor que você terá que pagar é de {multa_a_pagar}R$.')
else:
    print(f'Você não terá que pagar nenhuma multa pois não ultrapassou a quantidades em kg maximas estabelecidas pelo regulamento = {regulamento}kg.')

print('Programa encerrado com sucesso.')
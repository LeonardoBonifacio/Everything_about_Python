#Programa que lê o nome de uma pessoa e diz se ele(a) tem 'silva' no nome
from os import system
system('cls')
nome = str(input('Digite seu nome completo: '))

if('silva' in nome.casefold()):
    print('Seu nome é bem genérico por conter "silva".')
else:
    print('Parabens por não ter um nome genérico que contenha "silva".')
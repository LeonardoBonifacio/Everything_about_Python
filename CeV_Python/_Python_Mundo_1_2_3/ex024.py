#Programa que lê o nome de um cidade e diz se ela começa ou não com a palavra 'Santo'

from os import system
system('cls')

cidade = str(input('Digite o nome de sua cidade: '))


if(cidade.replace(' ','').casefold().startswith('santo')):
    print('Parabens por morar em uma cidade que começa com o nome "Santo"')
else:
    print('Sua cidade não começa com o nome "Santo".')
    
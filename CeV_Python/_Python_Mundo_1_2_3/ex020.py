from os import system
system('cls')

from random import shuffle #Função para embaralhar valores em uma lista

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
#Crei e coloquei os itens da lista, logo depois embaralhei os mesmos com a função shuffle

print(f'A ordem de apresentação do trabalho será\n{lista}.') 

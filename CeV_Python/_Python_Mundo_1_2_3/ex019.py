from os import system
system('cls')

from random import choice #Retorna valores aleatorios de uma lista

print('-=-' * 14, 'SORTEANDO ALUNOS PARA APAGAR O QUADRO' ,'-=-' * 14)

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

apagar_quadro = choice([aluno1, aluno2, aluno3, aluno4])

print(f'O aluno que vai apagar o quadro é  {apagar_quadro}.')
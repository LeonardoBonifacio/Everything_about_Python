#Programa que lê o nome de uma pessoa e mostra na tela o primeiro e o ultimos nome separadamente

from os import system
system('cls')

nome = str(input('Digite seu nome completo: '))

print(f'Seu nome completo é {nome.strip()}.')

nome_listado = nome.split()

print(f'Seu primeiro nome é {nome_listado[0]}.')

print(f'Seu último nome é {nome_listado[-1]}.')
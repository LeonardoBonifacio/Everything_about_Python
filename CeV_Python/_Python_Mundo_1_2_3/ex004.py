'''
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele
'''
from os import system
system('cls')

algo = input('Digite qualquer coisa: ')

print(f'O tipo primitivo de {algo} é {type(algo)}')

print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanúmerico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizada ou é um título? {algo.istitle()}')
print(f'É imprimível ? {algo.isprintable()}')
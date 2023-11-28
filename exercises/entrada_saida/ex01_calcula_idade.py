'''
Criar um programa que vai ler o ano de nascimento do usuário do seu sistema e vai informar quantos ele vai possuir em dezembro deste ano
'''

import os
os.system('cls')

ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = 2023
idade = ano_atual - ano_nasc

print(f'Você tem {idade} anos.')
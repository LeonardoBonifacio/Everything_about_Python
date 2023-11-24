'''
Este programa lê o ano de anscimento do usário e informa se ele é maior ou não
'''
import os 
os.system('cls')

ano_nasc =  int(input('Digite o seu ano de nascimento: '))
ano_atual = 2023
idade = ano_atual - ano_nasc

print(f'Você tem {idade} anos.')

if(idade >= 18):
    print('Parabens você é maior de idade')
else:
    print('Infelizmente você ainda não atingiu a maioridade.')

print('Programa finalizado com sucesso!')
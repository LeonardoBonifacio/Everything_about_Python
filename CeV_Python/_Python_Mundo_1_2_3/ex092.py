from os import system
system('cls')
from datetime import date

ano_atual = date.today().year
registro_geral = {}


registro_geral['Nome'] = str(input('Digite o nome do indivíduo: '))
registro_geral['idade'] =  ano_atual - int(input('Digite o seu ano de nascimento: '))
registro_geral['carteira de trabalho'] = int(input('Digite o número de sua ctps se você possui carteira de trabalho ou 0 se não possui: ')) 
if(registro_geral['carteira de trabalho'] != 0):
    registro_geral['ano de contratação'] = int(input('Digite o ano da sua contratação: '))
    registro_geral['salario'] = float(input('Digite o seu salário R$'))
    registro_geral['Idade  da aposentadoria'] = ((registro_geral['ano de contratação'] + 35) - ano_atual ) + registro_geral['idade']

print('-=-' * 20)
for k,v in registro_geral.items():
    print(f' -- {k} tem o valor {v}')

print(registro_geral)

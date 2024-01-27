from os import system
system('cls')
from datetime import date

print('----------SERÁ QUE É BISSEXTO?----------')

ano = int(input('Digite um ano qualquer ou digite 0 para analisar o ano atual: '))
if(ano == 0):
    ano = date.today().year
if(ano % 4 == 0  and ano % 100 != 0 or ano % 400 == 0 ):
    print(f'O ano {ano} É BISSEXTO')  
else:
    print(f'O ano {ano} não é BISSEXTO')
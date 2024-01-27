from os import system
system('cls')
from datetime import date

print('-=-' * 14, 'ALISTAMENTO MILITAR' ,'-=-' * 14)
sexo = int(input('[1] - Homem\n[2] - Mulher\n>>> '))
if(sexo == 1):
    ano_nasc = int(input('Digite o ano que você nasceu: '))
    idade = date.today().year - ano_nasc

    if(idade < 18):
        print(f'Ainda faltam {18 - idade} anos para você se alistar , pois você tem {idade} anos. O ano de seu alistamento será no ano de {date.today().year + (18 - idade)}, aguarde...')
    elif(idade == 18):
        print(f'Você já pode se alistar , pois , tem {idade} anos.')
    else:
        print(f'Já passaram {idade - 18} anos desde que você se alistou ou deixou de se alistar , pois , você tem {idade} anos. Seu alistamento foi no ano de {date.today().year - (idade - 18)}.')
elif(sexo == 2):
    print('O Alistamento Militar no Brasil so é possivel para homens.')
else:
    print('Valor inválido para sexo.')
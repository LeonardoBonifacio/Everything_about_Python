from os import system
system('cls')
from datetime import date

print('-=-' * 14, 'CATEGORIA EM NATAÇÃO' ,'-=-' * 14)

ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_nasc
print(f'O atleta tem {idade} anos')
if(idade <= 9 ):
    print('Você está classificado como atleta MIRIM.')
elif(idade <= 14):
    print('Você está classificado como atleta INFANTIL')
elif(idade <=19):
    print('Você está classificado como atleta JUNIOR')
elif(idade <= 25):
    print('Você está classificado como atleta SÊNIOR')
else:
    print('Você está classificado como atleta MASTER')
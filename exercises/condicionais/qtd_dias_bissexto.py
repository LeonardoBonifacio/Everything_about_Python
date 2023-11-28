from os import system 
system('cls')

mes = int(input('Digite o número do mês em questão: '))
ano = int(input('De que ano você se refere: '))

'''
 1 == Janeiro
 2 == Fevereiro
 3 == Março
 4 == Abril
 5 == Maio
 6 == Junho
 7 == Julho
 8 == Agosto
 9 == Setembro
 10 == Outubro
 11 == Novembro
 12 == Dezembro
'''

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0):
    if(mes == 1):
        print('Janeiro têm 31 dias.')
    elif(mes == 2):
        print('Fevereiro tem 29 dias,por ser ano bissexto.')
    elif(mes == 3):
        print('Março tem 31 dias')
    elif(mes == 4):
        print('Abril tem 30 dias')
    elif(mes == 5):
        print('Maio tem 31 dias')
    elif(mes == 6):
        print('Junho tem 30 dias')
    elif(mes == 7):
        print('Julho tem 31 dias')
    elif(mes == 8):
        print('Agosto tem 31 dias')
    elif(mes == 9):
        print('Setembro tem 30 dias')
    elif(mes == 10):
        print('Outubro tem 31 dias')
    elif(mes == 11):
        print('Novembro tem 30 dias')
    elif(mes == 12):
        print('Dezembro tem 31 dias')
    else:
        print('Você não digitou um valor válido para algum mês do ano.')
else:
    if(mes == 1):
        print('Janeiro tem 31 dias')
    elif(mes == 2):
        print('Fevereiro tem 28 dias')
    elif(mes == 3):
        print('Março tem 31 dias')
    elif(mes == 4):
        print('Abril tem 30 dias')
    elif(mes == 5):
        print('Maio tem 31 dias')
    elif(mes == 6):
        print('Junho tem 30 dias')
    elif(mes == 7):
        print('Julho tem 31 dias')
    elif(mes == 8):
        print('Agosto tem 31 dias')
    elif(mes == 9):
        print('Setembro tem 30 dias')
    elif(mes == 10):
        print('Outubro tem 31 dias')
    elif(mes == 11):
        print('Novembro tem 30 dias')
    elif(mes == 12):
        print('Dezembro tem 31 dias')
    else:
        print('Você não digitou um valor válido para algum mês do ano.')
        
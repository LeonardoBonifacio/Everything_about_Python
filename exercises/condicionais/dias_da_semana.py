from os import system
system('cls')

from calendar import *

valor_para_dia = input('[0] - Segunda feira\n[1] - Terça feira\n[2] - Quarta feira\n[3] - Quinta feira\n[4] - Sexta feira\n[5] - Sábado\n[6] - Domingo\n >> ')


if(valor_para_dia == '0'):
    print(day_name[0])
elif(valor_para_dia == '1'):
    print(day_name[1])
elif(valor_para_dia == '2'):
    print(day_name[2])
elif(valor_para_dia == '3'):
    print(day_name[3])
elif(valor_para_dia == '4'):
    print(day_name[4])
elif(valor_para_dia == '5'):
    print(day_name[5])
elif(valor_para_dia == '6'):
    print(day_name[6])
else:
    print('Valor inválido digitado.')

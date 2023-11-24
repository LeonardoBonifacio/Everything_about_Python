from os import system
system('cls')

data = str(input('Informe a data abaixo neste formato dd/mm/aaaa:\n-->>  '))
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if(ano < 0):
    print('ANO INVÁLIDO')
else:
    if(mes < 0 or mes > 12):
        print('MÊS INVÁLIDO')
    else:
        if(mes in [1, 3, 5, 7, 8, 10, 12]):
            if(dia < 0 or dia > 31):
                print('DIA INVÁLIDO')
            else:
                print('DATA VÁLIDA')
        elif(mes in [4, 6, 9, 11]):
            if(dia < 0 or dia > 30):
                print('DIA INVÁLIDO')
            else:
                print('DATA VÁLIDA')
        else:
            if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
                if(dia < 0 or dia > 30):
                    print('DIA INVÁLIDO')
                else:
                    print('DATA VÁLIDA')
            else:
                if(dia < 0 or dia > 29):
                    print('DIA INVÁLIDO')
                else:
                    print('DATA VÁLIDA')
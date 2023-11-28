def converterHorario(horario,AmOUPm):
    if(len(horario) == 5):
        horas = horario[0:2]
        minutos = horario[3:]
    else:
        horas = horario[0:1]
        minutos = horario[2:]
    if(int(horas) >= 1 and int(horas) <= 12 and AmOUPm == 'P'):
        if(horas == '1' ):
            horas = '13'
        elif(horas == '2'):
            horas = '14'
        elif(horas == '3'):
            horas = '15'
        elif(horas == '4'):
            horas = '16'
        elif(horas == '5'):
            horas = '17'
        elif(horas == '6'):
            horas = '18'
        elif(horas == '7'):
            horas = '19'
        elif(horas == '8'):
            horas = '20'
        elif(horas == '9'):
            horas = '21'
        elif(horas == '10'):
            horas = '22'
        elif(horas == '11'):
            horas = '23'
        elif(horas == '12'):
            horas = '00'
    elif(int(horas) >= 13 and int(horas) <= 24 and AmOUPm == 'A'):
        if(horas == '13'):
            horas = '1'
        elif(horas == '14'):
            horas = '2'
        elif(horas == '15'):
            horas = '3'
        elif(horas == '16'):
            horas = '4'
        elif(horas == '17'):
            horas = '5'
        elif(horas == '18'):
            horas = '6'
        elif(horas == '19'):
            horas = '7'
        elif(horas == '20'):
            horas = '8'
        elif(horas == '21'):
            horas = '9'
        elif(horas == '22'):
            horas = '10'
        elif(horas == '23'):
            horas = '11'
        elif(horas == '24'):
            horas = '00'
    else:
        return "Impossivel converter seu horário"
    return f"{horas}:{minutos}"
    

while(True):
    horas = str(input('Digite que horas são: (exemplo 14:30)'))
    if(len(horas) > 5 or len(horas) < 4):
        print('Horário inválido, por favor digite um horário correto..')
    elif(':' not in horas):
        print('Por favor digite o horário com os \":\"')
    elif(horas.isalpha()):
        print('Por favor digite apenas números e o sinal de \":\"')
    else:
        break
while(True): 
    manha_ou_tarde = str(input('Digite A para A.M. e P para P.M. : ')).strip()[0].upper()
    if(manha_ou_tarde in 'AP'):
        break
    else:
        print('Por favor digite A para A.M e P para P.M : ')
novas_horas = converterHorario(horas,manha_ou_tarde)
print(f'{horas} convertidas ficam {novas_horas}')

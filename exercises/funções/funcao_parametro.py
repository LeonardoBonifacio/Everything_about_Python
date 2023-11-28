from os import system
system('cls')

def cumprimentaUsuario(turnoDefinido):
    msg = ''
    if(turnoDefinido == '1'):
        msg = 'Bom dia'
    elif(turnoDefinido == '2'):
        msg = 'Boa tarde'
    elif(turnoDefinido == '3'):
        msg = 'Boa noite'
    else:
        print('Valor inválido')
    print(msg)

turno = input('Digite o turno:\n[1] - Manhã\n[2] - Tarde\n[3] - Noite\n-->  ')
cumprimentaUsuario(turno)
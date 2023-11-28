from os import system
system('cls')


meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

while(True):
    data = input('Por favor digite um data no formato dd/mm/aaaa  ->> ')
    if(len(data[0:2]) > 2):
        print('Por favor digite a quantidade certa de dígitos para cada campo da data')
    elif(len(data[3:5]) > 2):
        print('Por favor digite a quantidade certa de dígitos para cada campo da data')
    elif(len(data[6:]) != 4):
        print('Por favor digite a quantidade certa de dígitos para cada campo da data')
    elif(int(data[0:2]) > 31 or int(data[0:2]) < 1):
        print('Por favor tente novamente digitando um dia válido.')
    elif(int(data[3:5]) > 12 or int(data[3:5]) < 1):
        print('Por favor tente novamente digitando um mês válido.')
    else:
        break

print(f'Então a data escolhida foi {data[0:2]} de {meses[int(data[3:5]) - 1]} de {data[6:]}')
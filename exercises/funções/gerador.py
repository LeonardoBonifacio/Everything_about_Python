from os import system
system('cls')

def gerador(texto,qtd,borda):
    tamanho = len(texto)
    borda1 = '+---------==========---------+'
    borda2 = '~~~~~~~~~~::::::::::~~~~~~~~~~'
    borda3 = '<<<<<<<<<<---------->>>>>>>>>>'
    if(borda == 1):
        print(borda1)
    elif(borda == 2):
        print(borda2)
    elif(borda == 3):
        print(borda3)
    else:
        print('Não escolheu a borda correta')
    for c in range(qtd):
        print(f'{texto:^30}')
    if(borda == 1):
        print(borda1)
    elif(borda == 2):
        print(borda2)
    elif(borda == 3):
        print(borda3)
    else:
        print('Não escolheu a borda correta')
gerador('Leonardo',3,4)

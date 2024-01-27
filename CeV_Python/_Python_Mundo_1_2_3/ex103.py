from os import system
system("cls")


def ficha(nome,gols):
    if(nome == ''):
        nome = '<desconhecido>'
    if(gols == '' or gols.isalpha() == True):
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_do_jogador = str(input('Nome do Jogador: '))
numero_de_gols = str(input('Número de gols: '))
ficha(nome_do_jogador,numero_de_gols)

'''
jeito do guanabara
def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')

#Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if(g.isnumeric()):
    g = int(g)
else:
    g = 0
if(n.strip() == '):
    ficha(gol=g)
else:
    ficha(n,g)
'''
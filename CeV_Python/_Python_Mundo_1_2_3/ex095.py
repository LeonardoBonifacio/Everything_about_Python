from os import system
system('cls')


jogador = {}
lista_de_jogadores = []
lista_gols = []

while(True):
    jogador.clear()
    lista_gols.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    qtd_partidas = int(input(f'{jogador["Nome"]} jogou quantas partidas? '))
    for c in range(qtd_partidas):
        lista_gols.append(int(input(f'Fez quantos gols na {c + 1}° partida? ')))
    jogador['Gols'] = lista_gols.copy()
    jogador['Total'] = sum(lista_gols)
    lista_de_jogadores.append(jogador.copy())
    while(True):
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if(continuar in 'SN'):
            break
        print('Por favor, digite apenas S ou N...')
    if(continuar == 'N'):
        break
print('-=-' * 30) 
print('Cod',end=' ')
for chaves in jogador.keys():
    print(f'{chaves:<15}',end='')
print()
print('-' * 40)
for pos,elemento in enumerate(lista_de_jogadores):
    print(f'{(pos + 1):>3}',end=' ')
    for valor in elemento.values():
        print(f'{str(valor):<15}',end='')
    print()
print('-' * 40)
while(True):
    cod_jog = int(input('Mostrar dados de qual jogador? '))
    if(cod_jog == 999):
        break
    elif(cod_jog == 0  or cod_jog > len(lista_de_jogadores)):
        print(f'ERRO! Não existe jogador com código {cod_jog}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista_de_jogadores[cod_jog - 1]["Nome"]}')
        for pos,jogador in enumerate(lista_de_jogadores[cod_jog - 1]['Gols']):
            print(f'No {pos + 1}° jogo fez {jogador} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
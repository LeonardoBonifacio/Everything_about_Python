from os import system
system('cls')

jogador = {}
lista_gols = []
jogador['Nome'] = str(input('Digite o nome do jogador: '))
qtd_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for c in range(qtd_partidas):
    lista_gols.append(int(input(f'Quantos gols na partida {c + 1} ? ')))
jogador['gols'] = lista_gols.copy()
jogador['total'] = sum(lista_gols)
print('-=-' * 20)
print(jogador)
print('-=-' * 20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {jogador["Nome"]} jogou {qtd_partidas} partidas.')
for pos,gols in enumerate(lista_gols):
    print(f'    => Na partida {pos + 1}, fez {gols} gols.')
print(f'Foi um total de {sum(lista_gols)} gols.')

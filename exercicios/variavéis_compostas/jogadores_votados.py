from os import system
system('cls')
votos = []
jogadores = [0] * 23
print('-=-' * 10,'EMISSORA VARMINHO','-=-' * 10)
print('-=-' * 9,'QUEM FOI O MELHOR JOGADOR?','-=-' * 8)
while(True):
    print()
    jogador = int(input('Informe o número da camisa do jogador entre 1 e 23 ou 0 para sair da votação! '))
    if(jogador == 0):
        break
    elif(jogador > 23 or jogador < 0):
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    else:
        print('Voto registrado, obrigado por votar...')
        votos.append(jogador)
for voto in votos:
    jogadores[voto - 1] += 1
print(f'Foram computados: {len(votos)} votos.')
for pos,jogador in enumerate(jogadores):
    if(jogador > 0):
        print(f'O jogador {pos + 1} teve {jogador} votos, correspondendo a {jogador / len(votos):.2%} do total de votos.')
print(f'O melhor jogador foi o jogador {jogadores.index(max(jogadores)) + 1} com {max(jogadores)} votos, correspondendo a {max(jogadores) / len(votos):.2%} do total de votos.')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
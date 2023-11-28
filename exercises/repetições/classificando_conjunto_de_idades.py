'''Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

from os import system
system('cls')

idade = media = qtd_pessoas = 0

while(True):
    print('-=-' * 10,'CLASSIFICANDO IDADES', '-=-' * 10)
    qtd_pessoas += 1
    idade = int(input(f'Digite a idade da {qtd_pessoas}° pessoa: '))
    media += idade
    continuar = str(input('Digitar mais idades [S]im ou [N]ão >>> ')).strip().upper()[0]
    if(continuar == 'N'):
        break
    system('cls')
media /= qtd_pessoas

if(media > 0 and media <= 25):
    print(f'Aqui temos uma média de idades de {media:.2f} sendo assim uma turma mais jovem...')
elif(media > 25 and media <= 60):
    print(f'Aqui temos uma média de idades de {media:.2f} sendo assim  uma turma mais adulta...')
else:#Maior que 60
    print(f'Aqui temos uma média de idades de {media:.2f} sendo assim uma turma que está prestes a escorregar no sabonete pra cair no caixão.')
from os import system
system('cls')

altura = 0
print('Digite a altura de varia pessoas para saber a média entre elas.')
print('Para parar de colocar mais alturas digite (-1)')
count_pessoas = 0
soma_alturas = 0
while(altura != -1):
    altura = float(input('Digite a altura: '))
    if(altura != -1):
        count_pessoas = count_pessoas + 1
        soma_alturas = soma_alturas + altura

if(soma_alturas > 0):
    media = soma_alturas / count_pessoas
    print(f'A média de todas as altura digitadas foi de {media:.2f}.')
else:
    print('Não posso calcular a média se você não digitou nenhuma altura.')


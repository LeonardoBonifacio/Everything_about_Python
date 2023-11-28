from os import system
system('cls')
print('-=-' * 10,'CALCULANDO O VALOR DE UMA SEQUÊNCIA','-=-' * 10)
qtd_h = int(input('A sequência que será mostrada é H = 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/N\nPor favor digite quantas vezes essa sequência repetirá para que ela seja mostrada e somada: '))
h = 1
soma_h = 1
h_str = '1 + '
for n in range(2,qtd_h + 1):
    soma_h += h/n
    h_str += '1/' + str(n) + ' + '
print(f'A sequência ficou H = {h_str}',end = '... 1/N')
print(f'\nE sua soma deu {soma_h:.2f}')




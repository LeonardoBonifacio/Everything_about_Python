from os import system
system('cls')

print('==' * 20)
print(f'{"LISTAGEM DE PREÇO":^40}')#FORMATADO COM 40 ESPAÇOS E CENTRALIZADO
print('==' * 20)

tupla_de_compras = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for pos in range(0,len(tupla_de_compras)):
    if(pos % 2 == 0):#PRINTA OS VALORES PARES QUE SÃO OS PRODUTOS
        print(f'{tupla_de_compras[pos]:.<30}',end = '')#FORMATADO COM 30 ESPAÇOS PONTILHADOS ALINHADO A ESQUERDA E SEM QUEBRA DE LINHA NO FINAL
    else:#PRINTA OS VALORES IMPARES QUE SAO OS PREÇOS
        print(f'R${tupla_de_compras[pos]:>7.2f}')#FORMATADO COM 7 ESPAÇOS A DIREITA COM DUAS CASAS DECIMAIS
print('==' * 20)
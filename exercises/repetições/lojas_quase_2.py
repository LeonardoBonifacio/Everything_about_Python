from os import system
system('cls')
print('LOJAS QUASE 2 -- TABELA DE PREÇOS')
for qtd_produtos in range(1,51):
    print(f'{qtd_produtos:2d} - R${1.99 * qtd_produtos:.2f}')

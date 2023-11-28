from os import system
system('cls')

print('PANIFICADORA PÃO DE ONTEM')

preco_do_pao = float(input('Preço do pão R$'))

for qtd_paes in range(1,51):
    print(f'{qtd_paes:2d} - R${qtd_paes * preco_do_pao:.2f}')
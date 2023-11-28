import os 
os.system('cls')

qtd_produto = int(input('Digite a quantidade desse produto em estoque: '))
qtd_cliente = int(input('Digite a quantidade que o cliente deseja comprar: '))

if(qtd_cliente > qtd_produto):
    print(f'Você não pode comprar essa quantidade de produtos na nossa loja. Temos em estoque {qtd_produto} produtos e você deseja comprar {qtd_cliente} produtos.')
else:
    print(f'Você pode comprar essa quantidade de produtos na nossa loja. Temos em estoque {qtd_produto} produtos e você deseja comprar {qtd_cliente} produtos')
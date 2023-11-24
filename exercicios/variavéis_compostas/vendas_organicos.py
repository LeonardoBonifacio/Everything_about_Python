from os import system
system('cls')

estoque = {"Tomate": [1000, 2.30],
           "Alface": [500, 0.45],
           "Batata": [2001, 1.20],
           "Feijão": [100, 1.50],
           "Abóbora": [1000, 2.50]
           }
           
venda = []
while(True):
    while(True):
        produto = str(input('Digite o nome do produto que deseja comprar >>>(Tomate/Alface/Batata/Feijão/Abóbora)<<< \n>>>'))
        if(produto in estoque.keys()):
            break
        print('Por favor digite um produto dessa lista ou verifique se você está digitando exatamento com está sendo mostrado...')
    while(True):
        quantidade = int(input(f'Digite a quantide de {produto} que você quer comprar, máximo de {estoque[produto][0]} >>>'))
        if(quantidade > 0 and quantidade < estoque[produto][0]):
            break
        print(f'Por favor, digite um valor aceitável para a quantidade desejada de {produto} que você quer comprar...')
    venda.append([produto, quantidade].copy())
    while(True):
        resp = str(input('Comprar outros produtos [S/N]')).strip().upper()[0]
        if(resp in 'SN'):
            break
        print(f'ERRO ! Por favor digite apenas S ou N...')
    if(resp == 'N'):
        break

total = 0
print("Vendas:\n")
for operacao in venda:
    produto,quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo Total: {total:21.2f}\n')
print('Estoque:\n')
for chave,dados in estoque.items():
    print(f'Descrição: {chave}')
    print(f'Quantidaed: {dados[0]}')
    print(f'Preço: {dados[1]:6.2f}\n')
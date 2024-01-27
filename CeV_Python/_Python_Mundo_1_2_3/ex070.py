from os import system
system('cls')
qtd_produt_mais_mil = soma_da_compra = qtd_produtos = menor = 0
while(True):
    print('---' * 9)
    print('     LOJA SUPER BARATÃO     ')
    print('---' * 9)
    nome = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o preço desse produto R$'))
    qtd_produtos += 1
    soma_da_compra += preco
    if(qtd_produtos == 1 or preco < menor):
        menor = preco
        nome_do_mais_barato = nome
    if(preco > 1000):
        qtd_produt_mais_mil += 1
    while(True):
        continuar = str(input('Continuar comprando produtos? [S]im ou [N]ão >>> ')).strip().upper()[0]
        if(continuar == 'S' or continuar == 'N'):
            break
    if(continuar == 'N'):
        break
    system('cls')
print('---' * 9,'FIM DO PROGRAMA','---' * 9)
print(f'O total gasto com esse(s) {qtd_produtos} produto(s) foi R${soma_da_compra:.2f}')
print(f'Você comprou {qtd_produt_mais_mil} produtos que custam mais de R$1000,00')
print(f'O nome do produto mais barato foi {nome_do_mais_barato} e seu preço foi R${menor:.2f}')


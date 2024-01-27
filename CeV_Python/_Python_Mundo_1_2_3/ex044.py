from os import system
system('cls')

print('-=-' * 14, 'LOJAS DO TIO ZÉ ROBERTO' ,'-=-' * 14)

preco_produto = float(input('Digite o preço do produto que deseja comprar R$'))

forma_pagamento = int(input('[ 1 ] - À vista dinheiro/cheque\n[ 2 ] - À vista cartão\n[ 3 ] - Parcelado no cartão\n-> '))

if(forma_pagamento == 1):
    print(f'Quem paga à vista ganha desconto, novo valor = R${preco_produto - (10/100 * preco_produto)}')
elif(forma_pagamento == 2):
    print(f'Quem paga no débito ganha desconto, novo valor = R${preco_produto - (5/100 * preco_produto)}')
elif(forma_pagamento == 3):
    qtd_parcelas = int(input('Quer dividir em quantas parcelas: '))
    if(qtd_parcelas <= 0 or qtd_parcelas == 1 ):
        print(f'Não é possivel dividir em {qtd_parcelas} parcela(s), se deseja pagar no débito por favor  volte o Menu.')
    elif(qtd_parcelas == 2): 
        pagamento_mensal = preco_produto / qtd_parcelas
        print(f'Dividindo em até duas vezes no cartão o valor continua sem juros, R${preco_produto:.2f}\nFoi divido em {qtd_parcelas} parcelas de  R${pagamento_mensal:.2f}')
    elif(qtd_parcelas > 2 and qtd_parcelas <= 12):
        juros = preco_produto * (20/100) 
        preco_com_juros = preco_produto + juros
        pagamento_mensal = preco_com_juros / qtd_parcelas
        print(f'Será cobrado do valor do produto 20% de juros.\nNovo valor = R${preco_com_juros:.2f}\nR${juros:.2f} representam os juros de 20%\nFoi dividido em {qtd_parcelas} parcelas de R${pagamento_mensal:.2f}.')
    else:
        print('\033[1mNão é possivel dividir em mais de 12 parcelas\033[m.')
else:
    print('\033[1mOPÇÃO INVÁLIDA DE PAGAMENTO\033[m')
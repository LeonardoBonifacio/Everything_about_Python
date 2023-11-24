from os import system
system('cls')

print('-=--=- HIPERMERCADO TABAJARA -=--=- ')   
tipo_carne = int(input('[ 1 ] - Filé Duplo\n[ 2 ] - Alcatra\n[ 3 ] - Picanha\n>>>  '))
if(tipo_carne < 1 or tipo_carne > 3):
    print('Tipo de carne inválida')
else:
    kg_carne = int(input('Digite quantos kg de Carne: '))
    cartao_tabajara = str(input('Vai pagar no Cartão Tabajara: [SIM] ou [NÃO]\n>>>  ')).strip().upper()
    if(tipo_carne == 1):
        carne = 'File Duplo'
        if(kg_carne <= 5):
            preco_carne = kg_carne * 4.90
        elif(kg_carne > 5):
            preco_carne = kg_carne * 5.80
    elif(tipo_carne == 2):
        carne = 'Alcatra'
        if(kg_carne <= 5):
            preco_carne = kg_carne * 5.90
        elif(kg_carne > 5):
            preco_carne = kg_carne * 6.80
    elif(tipo_carne == 3):
        carne = 'Picanha'
        if(kg_carne <= 5):
            preco_carne = kg_carne * 6.90
        elif(kg_carne > 5):
            preco_carne = kg_carne * 7.80
    print(f'Tipo de carne: {carne}\nQuantidade de Carne: {kg_carne}kg\nPreco Total R${preco_carne:.2f}\nPagou com cartão tabajara: {cartao_tabajara}')
    if(cartao_tabajara == 'SIM'):
        preco_desconto = preco_carne - (preco_carne * 0.05)
        print(f'Por pagar com o cartão tabajara você ganhou 5% desconto, novo preço R${preco_desconto:.2f}\nValor do desconto: R${(preco_carne * 0.05):.2f}')


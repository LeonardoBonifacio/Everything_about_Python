from os import system
system('cls')
while(True):
    print('-=-' * 10,'LOJA DO SEU MANOEL - ELE QUER O SEU ANEL',10 * '-=-')
    print('[Digite 0 se não quer comprar mais]')
    dinheriro_fornecido = total_compra = cont = 0
    while(True):
        cont += 1
        preco = float(input(f'Preço do {cont}° produto R$'))
        total_compra += preco
        if(preco == 0):
            while(True):
                dinheiro_fornecido = float(input(f'A compra total dos {cont - 1} produtos deu R${total_compra:.2f}, vai precisar de troco pra quanto R$ '))
                if(dinheiro_fornecido >= total_compra):
                    print(f'Pois tome seu troco então R${dinheiro_fornecido - total_compra:.2f}')
                    print('Compra finalizada com sucesso')
                    break
                else:
                    print('Ta querendo me dar calote doido?\nMe de um valor acima do total da compra pra que eu possa te dar um troco justo.')
            break
    proximo = str(input('Proximo cliente? [S]im ou [N]ão >>> ')).strip().upper()[0]
    if(proximo == 'N'):
        break
    else:
        system('cls')
print('CAIXA ENCERRADO COM SUCESSO')
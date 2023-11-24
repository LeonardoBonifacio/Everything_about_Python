from os import system
preco_total = 0
while(True):
    system('cls')
    while(True):
        print('===' * 10,'LANCHONETE DO SEU OVO','===' * 10)
        cod_lanche = int(input('[100] - Cachorro Quente    Valor      R$1,20\n[101] - Bauru Simples      Valor      R$1,30\n[102] - Bauru com Ovo      Valor      R$1,50\n[103] - Hambúrguer         Valor      R$1,20\n[104] - Chessbúrguer       Valor      R$1,30\n[105] - Refrigerante       Valor      R$1,00\n>>> '))
        if(cod_lanche not in [100, 101, 102, 103, 104, 105]):
            print('Valor inválido para as opções do Menu...')
            input('[ENTER] - Para escolher uma nova opção...')
            system('cls')
        else:
            break
    while(True):
        qtd = int(input(f'Quer quantos lanches {cod_lanche}? '))
        if(qtd <= 0):
            print('Por favor, informe um valor maior que 0...')
        else:
            break
    if(cod_lanche == 100):
        preco_total += 1.20 * qtd
    elif(cod_lanche == 101):
        preco_total += 1.30 * qtd
    elif(cod_lanche == 102):
        preco_total += 1.50 * qtd
    elif(cod_lanche == 103):
        preco_total += 1.20 * qtd
    elif(cod_lanche == 104):
        preco_total += 1.30 * qtd
    elif(cod_lanche == 105):
        preco_total += 1 * qtd
    pedir_mais = str(input('Deseja mais coisas do nosso MENU? [S]im ou [N]ão ')).strip().upper()[0]
    if(pedir_mais == 'N'):
        system('cls')
        break
print(f'O valor total do seu pedido deu R${preco_total:.2f}, bem barato né...')
print('Volte sempre a LANCHONETE DO SEU OVO')
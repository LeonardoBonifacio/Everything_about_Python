from os import system
system('cls')

print('-=-' * 14, 'CALCULANDO PREÇO FINAL DA COMPRA' , '-=-' * 14)

valor_total = float(input('Digite o valor total da compra R$'))
cartao_sim_nao = int(input('[1] - Pagar com cartão\n[2] - Pagar a vista\n->     '))

if(cartao_sim_nao == 1):
    desconto = 2/100
    if(valor_total <=0):
        print('Valor da compra inválido')
    elif(valor_total <= 100):
        print(f'Você ganhou apenas 2% de desconto por optar pagar com cartão de credito, o valor final foi de {valor_total -(desconto * valor_total):.2f}')
    elif(valor_total > 100 and valor_total <= 500):
        desconto += 5/100
        print(f'Você ganhou um desconto de 7% , por optar pagar com cartão e pelo valor da compra, valor final = {valor_total - (desconto * valor_total):.2f}')
    elif(valor_total > 500):
        desconto += 10/100
        print(f'Você ganhou um desconto de 12%, por optar pagar com cartão e pelo valor da comprar, valor final = {valor_total - (desconto * valor_total):.2f}')
elif(cartao_sim_nao == 2):
    desconto = 0
    if(valor_total <=0):
        print('Valor da compra inválido')
    elif(valor_total <= 100):
        print(f'Você não ganhou descontos, o valor final foi de {valor_total:.2f}')
    elif(valor_total > 100 and valor_total <= 500):
        desconto += 5/100
        print(f'Você ganhou um desconto de 5% , por optar pagar com cartão e pelo valor da compra, valor final = {valor_total - (desconto * valor_total):.2f}')
    elif(valor_total > 500):
        desconto += 10/100
        print(f'Você ganhou um desconto de 10%, por optar pagar com cartão e pelo valor da comprar, valor final = {valor_total - (desconto * valor_total):.2f}')
else:
    print('Valor inválido para forma de pagamento.')
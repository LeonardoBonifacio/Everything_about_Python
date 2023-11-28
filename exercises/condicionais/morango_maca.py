from os import system
system('cls')

print('-=--=- FRUTAS DA DONA JANI -=--=-')

kg_morango = int(input('Digite quantos kg de morango você vai querer: '))
kg_maca = int(input('Digite quantos kg de maça você vai querer: '))
if(kg_morango <= 5):
    preco_morango = 2.50 * kg_morango
elif(kg_morango > 5):
    preco_morango = 2.20 * kg_morango
if(kg_maca <= 5):
    preco_maca = 1.80 * kg_maca
elif(kg_maca > 5):
    preco_maca = 1.50 * kg_maca
preco_total = preco_maca + preco_morango 
print(f'Você comprou {kg_maca}kg de maça e {kg_morango}kg de morango , seus respectivos preços foram R${preco_maca:.2f} e R${preco_morango:.2f}, com isso o preço total foi de R${preco_total:.2f}')
if(kg_maca + kg_morango > 8 or preco_total > 25):
    preco_total -= preco_total * 0.10
    print(f'E por comprar mais de 8kg de fruta ou por ter ultrapassado R$25,00 em compras, você ainda ganhou um desconto de 10%, novo preço R${preco_total:.2f}')

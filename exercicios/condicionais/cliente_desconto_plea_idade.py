'''
Este programa lê a idade do cliente e,caso ele tenha mais de 50 anos ele informa que o cliente tem direito a 10% na  de desconto na loja
Além disso. ele lê o valor da compra e infroma:
-Valor da compra
-Valor do desconto
-Valor da pagar
'''
import os
os.system('cls')

print('-----LOJINHA DO CRAUDIO-----')

idade = int(input('Digite sua idade por favor: '))

if(idade >= 50):
    print(f'Parabens, o senhor ganhou 10% de desconto em nossa loja, pois tem idade maior/igual a 50 anos . ')
    valor_compra = int(input('Qual foi o valor da sua compra: '))
    valor_do_desconto = valor_compra*10/100
    valor_a_pagar = valor_compra - valor_do_desconto 
    print(f'A sua compra foi de R${valor_compra:.2f} e o valor do desconto para ela foi de R${valor_do_desconto:.2f}  logo o senhor pagará com o desconto o valor de R${valor_a_pagar:.2f}.')
else:
    print('Infelizmente você não ganhou o desconto de nossa loja.')

print('Programa finalizado com sucesso!')
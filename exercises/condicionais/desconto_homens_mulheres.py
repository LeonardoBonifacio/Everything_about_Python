'''
A proprietária de um empresa de software recebeu uma demanda onde uma gerente de uma loja gostaria de criar u sistema de desconto priorizando mulheres com mais de 45 anos. A ideia parte de conceder a elas um desconto de 45% do valor das compras, sendo que o desconto sempre gira em torno de valores acima de 250 reais(ou seja so há desconto com valores acima desse preço). Para outras pessoas, sejam , mulheres ou homens, o sistema de desconto funcionará desta forma:
Acima de 250 reais
Acima de 45 anos: 45% se mulher e 0% se homem
Acima de 30 anos: 15% se mulher e 10% se homem.
Acima de 20 anos: 10% se mulher e 05% se homem.

Desenvolva essa função no python, teste e envie a resposta via formulário de resposta no link abaixo
'''

import os
os.system('cls')

print('==========CONCEDENDO DESCONTOS==========')
valor_compra = float(input('Digite o valor da compra: '))

if(valor_compra > 250):
    print('Você tem direito a desconto, parabens.')
    genero = input('[1] - Homem\n[2] - Mulher\n>> ')
    if(genero == '1'):
        print('Desconto para homens sendo aplicado')
        idade = int(input('Digite sua idade: '))
        if(idade > 30):
            print('Desconto de 10% aplicado')
            desconto = valor_compra - (valor_compra*(10/100))
            print(f'O valor da compra foi de R${valor_compra:.2f} e com o desconto de 10% o valor final da compra foi de R${desconto:.2f} ')
        elif(idade > 20):
            print('Desconto de 5% aplicado')
            desconto = valor_compra - (valor_compra*(5/100))
            print(f'O valor da compra foi de R${valor_compra:.2f} e com o desconto de 5% o valor final da compra foi de R${desconto:.2f}')
        else:
            print('Mesmo sendo homem, sua idade não está apta a receber descontos.')
    elif(genero == '2'):
        print('Desconto para mulheres aplicado')
        idade = int(input('Digite sua idade: '))
        if(idade > 45):
            print('Desconto de 45% aplicado')
            desconto = valor_compra - (valor_compra*(45/100))
            print(f'O valor da compra foi de R${valor_compra:.2f} e com o desconto de 45% o valor final da compra foi de R${desconto:.2f}')
        elif(idade > 30):
            print('Desconto de 15% aplicado')
            desconto = valor_compra - (valor_compra*(15/100))
            print(f'O valor da compra foi de R${valor_compra:.2f} e com o desconto de 15% o valor final da compra foi de R${desconto:.2f}')
        elif(idade > 20):
            print('Desconto de 10% aplicado')
            desconto = valor_compra - (valor_compra*(10/100))
            print(f'O valor da compra foi R${valor_compra:.2f} e com o desconto de 10% o valor final da compra foi de R${desconto:.2f}')
        else:
            print('Mesmo sendo mulher, sua idade não está apta a receber descontos.')
    else:
        print('Valor inválido')
else:
    print('Você não tem direito a desconto.')
    
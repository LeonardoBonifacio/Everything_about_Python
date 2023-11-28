from os import system
system('cls')
'''
valor_inicial_divida = float(input('Qual o valor inicial da dívida? '))
juro_mensal = float(input('Porcentagem de juros mensais: '))
valor_inicial_divida2 = valor_inicial_divida
valor_mensal_pago = float(input('Você pretende paga quanto mensalmente? R$'))
numero_meses = total_pago = total_juros_pagos = 0
juros = 0

while(valor_inicial_divida > 0):
    numero_meses += 1

    total_pago += valor_mensal_pago

    juros = valor_inicial_divida * (juro_mensal/100)

    valor_inicial_divida += juros

    valor_inicial_divida -= (valor_mensal_pago)

print(f'O número de meses para pagar essa dívida foi de {numero_meses}')
print(f'O total pago dessa dívida foi de R${total_pago:.2f}')
print(f'O total de juros pagos desa dívida foi de R${total_pago - valor_inicial_divida2}')

'''
#Ota forma de fazer esse código

divida = float(input('Dívida:  '))
taxa = float(input('Juros (Ex: 3 para 3%): '))
pagamento = float(input('Pagamento mensal R$'))
mes = 1

if(divida * (taxa/100) > pagamento):
    print('Sua dívida nunca será paga, pois os juros são superiores ao pagamento mensal')
else:
    saldo = divida
    juros_pago = 0
    while(saldo > pagamento):
        juros = saldo * (taxa/100)
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print(f'Saldo de dívida no mês {mes} é de R${saldo:.2f}')
        mes += 1
    print(f'Para pagar uma dívida de R${divida:.2f}, a {taxa:.2f} % de juros')
    print(f'Você precisará de {mes - 1} meses, pagando um total de R${juros_pago:.2f} de juros.')
    print(f'No último mês, você teria um saldo residual de R${saldo:.2f} a pagar')

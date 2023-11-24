from os import system
system('cls')

print( '-=-' * 10,'SIMULADOR DE POUPANÇA', '-=-' * 10)

deposito_inicial = float(input('Qual será o deposito inicial? R$'))
deposito_mensal = float(input('Qual o depósito mensal? R$'))
taxa_de_juros = float(input('Qual é a taxa de juros da poupança?(%) >>'))
total_com_juros = 0
final = deposito_inicial 
for mes in range(1,25):
    final = final + deposito_mensal +  ((final + deposito_inicial) * ((taxa_de_juros/100)/12))
    print(f'{mes}° mes R${(final):.2f}')
total_com_juros = final - deposito_inicial
print(f'O total ganho com juros nesses 24 meses foi de R${total_com_juros:.2f}')
    


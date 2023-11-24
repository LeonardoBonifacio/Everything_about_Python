from os import system
system('cls')

print('='*20,'VOCÊ VAI MORRER ANTES DO NATAL','='*20)

cigarros_fumados_por_dia = int(input('Digite quantos cigarros você fuma por dia: '))
anos_que_fuma = int(input('Têm quantos anos que você fuma? '))

#Perde 10min de vida a cada cigarro
#Exibir o total de dias que ele perdeu de vida em dias.

'''
Cada dia tem 24h ou 1440 min
Cada ano tem 365 dias  ou 8760h ou 525,600min
'''

total_cigarros_fumado = cigarros_fumados_por_dia * (anos_que_fuma*365)

minutos_de_vida_perdidos = total_cigarros_fumado * 10

dias_de_vida_perdidos = minutos_de_vida_perdidos / 1440

print(f'Saiba que por fumar {cigarros_fumados_por_dia} cigarros por dia e já ter fumado por {anos_que_fuma} anos , você ja perdeu {dias_de_vida_perdidos:.2f} dias de vida.')
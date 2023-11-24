'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1L para cada 3m² e que a tinta é vendida em latas de 18L, que custam R$80,00
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
'''

from os import system 
system('cls')

# 3m² por litro cobertura da tinta
cobertura_tinta = 3
#Capacidade da lata 18 litros de tinta
capacidade_lata = 18
#Preço da lata 80 reais
preco_lata = 80.0

tamanho_area = float(input('Digite o tamanho da área a ser pintada (em m²): '))

litros = tamanho_area/cobertura_tinta
latas_inteiras = int(litros/capacidade_lata)
if(litros%capacidade_lata != 0):
    latas_inteiras += 1

valor_total = latas_inteiras * preco_lata

print(f'A quantidade de latas necessária é de {latas_inteiras}\nO preço a se pagar pelas latas é de R${valor_total:.2f}\nA quantidade de litros que você vai usar para pintar essa área de {tamanho_area}m² é de {litros:.2f}L')
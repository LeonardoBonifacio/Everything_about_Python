from os import system
system('cls')
total = 0
print('-=-' * 10,'CALCULANDO O TANTO QUE SE DESPERDIÇOU EM DINHERIO COM CDS','-=-' * 10)

qtd_cds = int(input('Quantos cds você têm em sua coleção? '))

for cds in range(1,qtd_cds + 1):
    gastou = float(input(f'Gastou quanto no {cds}° cd? '))
    total += gastou
print(f'O total gastou com todos esse {qtd_cds} cds foi de R${total:.2f}.')
total /= qtd_cds
print(f'E o valor médio gasto com cada um deles foi de {total:.2f}')

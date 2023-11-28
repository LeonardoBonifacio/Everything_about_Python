from os import system
system('cls')

qtd = int(input('Vai fornecer quantos números para saber a média: '))
media = 0
for num in range(1,qtd + 1):
    numeros_fornecidos = int(input(f'{num}° número: '))
    media += numeros_fornecidos
media /= qtd
print(f'A média dos {qtd} números fornecidos foi de {media:.2f}')
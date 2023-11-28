from os import system
system('cls')
qtd_numeros = 0
continuar = ''
somatorio = 0
qtd_par = 0
print('ANALISANDO UNS NÚMEROS AEE')
while(continuar != 'N'):
    num = int(input(f'Digite o {qtd_numeros + 1}° número: '))
    qtd_numeros += 1
    continuar = str(input('Continuar ? [S] ou [N] >>> ')).strip().upper()
    somatorio += num
    if(qtd_numeros == 1):
        menor_num = num
    else:
        if(num < menor_num):
            menor_num = num
    if(num % 2 == 0):
        qtd_par += 1
media = somatorio / qtd_numeros
print(f'O somatório entre todos os valores é de {somatorio}')
print(f'O menor número digitado foi {menor_num}')
print(f'A média entre todos os valores digitados foi de {media:.1f}')
print(f'A quantidade de números pares digitados foi de {qtd_par}')
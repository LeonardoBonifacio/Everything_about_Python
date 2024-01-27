from os import system
system('cls')

continuar = 'S'
media = qtd_num = 0
while(continuar == 'S'):
    print('-=--=--=- ANALISANDO MÉDIA/MAIOR/MENOR -=--=--=-')
    num = int(input('Digite um número: '))
    qtd_num += 1
    media += num
    if(qtd_num == 1):
        menor = maior = num
    else:
        if(num > maior):
            maior = num
        if(num < menor):
            menor = num
    continuar = str(input('Quer digitar mais números? [S] ou [N]')).strip().upper()[0]
    system('cls')
media /= qtd_num
print(f'Quantidade de números digitados: {qtd_num}')
print(f'Média: {media:.2f}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
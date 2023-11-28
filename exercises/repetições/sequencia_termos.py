from os import system
system('cls')
primeiro_termo = 1
segundo_termo = 1
soma = 0
qtd_termos = int(input('Será mostrada uma sequencia de termos --> S = 1/1 + 2/3 + 3/5 ...\nPor favor digite a quantidade de termos que você quer ver dessa série: '))
print('S = ',end = ' ')
for termos in range(qtd_termos):
    print(primeiro_termo,'/',segundo_termo,' + ',end = '')
    soma += primeiro_termo/segundo_termo
    primeiro_termo += 1
    segundo_termo += 2
print(' NADA')
print(f'A soma entre todos esses termos na forma decimal é de {soma:.2f}')
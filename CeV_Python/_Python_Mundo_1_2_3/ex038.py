from os import system
system('cls')

print('-=-' * 14, 'MAIOR OU IGUAL' ,'-=-' * 14)

numA = int(input('Digite um número inteiro: '))
numB = int(input('Digite outro número inteiro: '))

if(numA > numB):
    print(f'O primeiro valor digitado({numA}) é maior.')
elif(numB > numA):
    print(f'O segundo valor digitado({numB}) é maior.')
else:
    print(f'Não existe valor maior, os dois números são iguais, {numA} = {numB}')

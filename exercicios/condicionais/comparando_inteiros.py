from os import system
system('cls')

numA = int(input('Digite um número inteiro: '))
numB = int(input('Digite outro número inteiro: '))

if(numA > numB):
    print(f'{numA} é maior do que {numB}')
elif(numB > numA):
    print(f'{numB} é maior do que {numA}')
else:
    print(f'{numA} é igual a {numB} , não existe valor maior.')
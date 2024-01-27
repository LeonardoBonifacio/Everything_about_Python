from os import system
system('cls')

print('----------DESCOBRINDO MAIOR E MENOR----------')

numA = int(input('Digite um número qualquer: '))
numB = int(input('Digite outro número qualquer: '))
numC = int(input('Digite mais um número qualquer: '))



if(numA > numB and numA > numC):
    print(f'{numA} foi o maior número digitado.')
elif(numB > numA and numB > numC):
    print(f'{numB} foi o maior número digitado.')
elif(numC > numA and numC > numB):
    print(f'{numC} foi o maior número digitado.')
    
if(numA < numB and numA < numC):
    print(f'{numA} foi o menor número digitado')
elif(numB < numA and numB < numC):
    print(f'{numB} foi o menor número digiitado')
elif(numC < numA and numC < numB):
    print(f'{numC} foi o menor número digitado')
else:
    print('Todos os valores digitados foram iguais.')
'''
menor = numA
if(numB < numC and numB < numA):
    menor = numB
elif(numC < numB and numC < numA):
    menor = numC
print(f'O menor valor digitado foi {menor}.)

maior = numA 
if(numB > numC and numB > numA):
    maior = numB
elif(numC > numB and numC > numA):
    maior = numC
print(f'O maior valor digitado foi {maior}.)
    
'''

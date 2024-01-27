from os import system
system('cls')

print('-=-' * 10, 'DESCOBRINDO O MAIOR E MENOR PESO' ,'-=-' * 10)
maior = 0
menor = 700
for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}° pessoa: '))
    if(peso < menor):
        menor = peso
    if(peso > maior):
        maior = peso
print(f'O menor peso foi de {menor:.2f}kg\nO maior foi de {maior:.2f}kg ')

'''

Jeito que o guanabara explicou

maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}° pessoa: '))
    if(pessoa == 1):
        maior = peso
        menor = peso
    else:
        if(peso > maior):
            maior = peso
        if(peso < menor):
            menor = peso
print(f'o maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi de {menor}kg.')

'''
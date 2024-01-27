from os import system
system('cls')


lista_completa = []
lista_pares = []
lista_impares = []
print('-=-' * 10,'ANALISANDO VALORES EM LISTAS','-=-' * 10)
while(True):
    num = int(input('Digite um número inteiro qualquer: '))
    lista_completa.append(num)
    if(num % 2 == 0):
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    continuar = str(input('Quer continuar a digitar valores? [S]im ou [N]ão >>>')).strip().upper()[0]
    if(continuar == 'N'):
        break

print(f'A)Aqui está a lista completa dos valores digitados: {lista_completa}.')
print(f'B)Aqui está uma lista com os valores pares digitados: {lista_pares}.')
print(f'C)Aqui está uma lista com os valores impares digitados: {lista_impares}.')
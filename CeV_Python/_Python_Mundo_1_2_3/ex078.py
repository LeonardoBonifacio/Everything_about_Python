from os import system
system('cls')
lista_valores = list()
for pos in range(5):
    lista_valores.append(int(input(f'Digite um valor para a posição {pos}: ')))

maior = max(lista_valores)
menor = min(lista_valores)

print(f'Você digitou os valores {lista_valores}.')
print(f'O maior valor digitado foi {maior} nas posições ',end = ' ')
for pos,valor in enumerate(lista_valores):
    if(valor == maior):
        print(f'{pos}...',end = ' ')
print(f'\nO menor valor digitado foi {menor} nas posições ',end = ' ')
for pos,valor in enumerate(lista_valores):
    if(valor == menor):
        print(f'{pos}...',end = ' ')

'''
Jeito do guanabara

listanum = []
mai = 0
men = 0

for c in range(0,5):
    listanum.append(int(input('Digite um valor para a posição {c}: ')))
    if(c == 0):
        mai = men = listanum[c]
    else:
        if(listanum[c] > mai):
            mai = listanum[c]
        if(listanum < men):
            men = listanum[c]
print('-=' * 30)
print(f'Você digitou os calores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições',end = '')
for i,v in enumerate(listanum):
    if(v == mai):
        print(f'{i}...',end = '')
print()
print(f'O menor valor digitado foi {men} nas posições ',end = '')
for i,v in enumerate(listanum):
    if(v == men):
        print(f'{i}...',end = '')
print()

'''
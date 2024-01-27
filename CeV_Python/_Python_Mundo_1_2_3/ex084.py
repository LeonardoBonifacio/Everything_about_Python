from os import system
system('cls')

pessoas = []
pessoa = []
while(True):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Continuar? [S/N]')).strip().upper()[0]
    if(resp == 'N'):
        break
maior = 0
menor = 200
for pessoa in pessoas:
    if(pessoa[1] > maior):
        maior = pessoa[1]
    if(pessoa[1] < menor):
        menor = pessoa[1]

print(f'A)Foram cadastradas {len(pessoas)} pessoas.')
print(f'B)O maior peso foi de: {maior:.2f}KG que foram de ',end = '')
for peso in pessoas:
    if(peso[1] == maior):
        print(f'[{peso[0]}]',end = '')
print(f'\nC)O menor foi foi de {menor:.2f}KG que foram de ',end = '')
for peso in pessoas:
    if(peso[1] == menor):
        print(f'[{peso[0]}]',end = '')

'''
princ = []
temp = []
mai = men = 0

while(True):
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if(len(princ) == 0):
        mair = men = temp[1]
    else:
        if(temp[1] > mai):
            mai = temp[1]
        if(temp[1] < men):
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if(resp in 'Nn'):
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ',end = '')
for p in princ:
    if(p[1] == mai):
        print(f"[{p[0]}],end = ''")
print()
print(f'O menor peso foi de {men}kg. Peso de ',end ='')
for p in princ:
    if(p[1] == men):
        print(f'[{p[0]}]',end = '')
print()
'''
from os import system
system('cls')
usuarios = ['Alenxandre', 'Anderson', 'Antonio', 'Carlos', 'Cesar', 'Rosemary']
bts = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]
kb = []
mb = []
for bt in bts:
    kb.append(bt/1024)
for kbs in kb:
    mb.append(kbs / 1024)
print(f'{"Uso do espaço em disco dos usuários":^70}')
print('------------------------------------------------------------------------')
print(f'{"Nr.":<4}{"Usuário":^15}{"Espaço Utilizado":^26}{"% do uso":^16}')
for pos, nomes in enumerate(usuarios):
    print(f'{(pos + 1):<4}    {nomes:<10} {mb[pos]:>18.2f} MB {(mb[pos]/sum(mb)):>16.2%}')
print(f'Espaço total ocupado: {sum(mb):.2f}MB')
print(f'Espaço médio ocupado: {(sum(mb)/6):.2f}MB')

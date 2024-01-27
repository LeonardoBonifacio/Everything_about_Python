from os import system
system('cls')

matriz = [[], [], []]
pos = [0,0]
for num in range(9):
    if(len(matriz[0]) < 3):
        matriz[0].append(int(input(f'Digite um valor para {pos}: ')))
        pos[1] += 1
    elif(len(matriz[1]) < 3):
        pos[0] = 1
        if(pos[1] >= 3):
            pos[1] = 0
        matriz[1].append(int(input(f'Digite um valor para {pos}: ')))
        pos[1] += 1
    elif(len(matriz[2]) < 3):
        pos[0] = 2
        if(pos[1] >= 3):
            pos[1] = 0
        matriz[2].append(int(input(f'Digite um valor para {pos}: ')))
        pos[1] += 1
print('-=' * 30)
for num in matriz[0]:
    if(num == matriz[0][-1]):
        print(f'[{num:^5}]')
    else:
        print(f'[{num:^5}]',end = ' ')
for num in matriz[1]:
    if(num == matriz[1][-1]):
        print(f'[{num:^5}]')
    else:
        print(f'[{num:^5}]',end = ' ')
for num in matriz[2]:
    print(f'[{num:^5}]',end = ' ')
print('-=' * 30)



#Solução do guanabara
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
print('-=' * 30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end = '')
    print()
'''


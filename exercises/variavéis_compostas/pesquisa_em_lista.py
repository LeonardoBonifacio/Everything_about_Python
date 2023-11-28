from os import system
system('cls')

l = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
x = 0
y = 0
lista_achados = []
while(True):
    while(True):
        if(x == 4):
            break
        if(l[x] == p):
            lista_achados.append(l[x])
            break
        x += 1
    while(True):
        if(y == 4):
            break
        if(l[y] == v):
            lista_achados.append(l[y])
            break
        y += 1
    if(x or y == 4):
        break
if(p in lista_achados):
    if(p == lista_achados[0]):
        print(f'{p} foi o primeiro número achado na posição {x}')
    else:
        print(f'{p} foi encontrado na posição {x}')
else:
    print(f'{p} não foi encontrado')

if(v in lista_achados):
    if(v == lista_achados[0]):
        print(f'{v} foi o primeiro número achado na posição {y}')
    else:
        print(f'{v} foi encontrado na posição {y}')
else:
    print(f'{v} não foi encontrado')
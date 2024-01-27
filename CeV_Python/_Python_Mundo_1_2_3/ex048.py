from os import system
system('cls')

s = 0
cont = 0
for c in range(1,501):
    if(c % 3 == 0 and c % 2 != 0 ):
            s += c
            cont += 1
print(f'A soma de todos os {cont} números ímpares e multiplos de 3 entre 1 e 500 é: {s}')

'''
Também poderia fazer assim para ocupar menos processamento

for c in range(1,501,2):
    if(c % 3 == 0):
        s += c
        c += 1
print(f'A soma de todos os {cont} números ímpares e multiplos de 3 entre 1 e 500 é: {s})
'''
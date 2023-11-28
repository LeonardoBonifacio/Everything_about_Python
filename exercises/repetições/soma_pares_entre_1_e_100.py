from os import system
system('cls')
cont = 0
soma = 0
for pares in range(2,102,2):
    soma += pares
    cont += 1
print(f'A soma dos {cont} números pares entre 1 e 100 é {soma}')
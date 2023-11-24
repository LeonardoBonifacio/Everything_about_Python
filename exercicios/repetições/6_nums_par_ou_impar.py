from os import system
system('cls')

pares = 0
impares = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}° número inteiro: '))
    if(num % 2 == 0):
        pares += 1
    else:
        impares += 1
print(f'Dos 6 números digitados, {pares} são pares e {impares} são impares.')

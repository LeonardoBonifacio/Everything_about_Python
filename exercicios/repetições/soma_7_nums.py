from os import system
system('cls')

soma = 0
for c in range(1,8):
    num = int(input(f'Digite o {c}° número: '))
    soma += num
print(f'A soma desses 7 números digitados é {soma}.')
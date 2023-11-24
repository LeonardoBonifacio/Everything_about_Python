from os import system
system('cls')

soma = 0
'''lista = []
for num in range(6,102,2):
    soma += num
    lista.append(num)
print(f'A soma dos números pares entre 6 e 100 {lista}.')
print(f'é igual a {soma}')
'''
for nums in range(500,0,-50):
    soma += nums
print(f'A soma dos números divisiveis por 50 entre 500 e 0 é {soma}')

from os import system
system('cls')

a = []

for numero in range(1,11):
    num = int(input(f'Digite o {numero}° número: '))
    a.append(num ** 2)
print(f'A soma dos quadradros de todos os números digitados é {sum(a)}.')

'''
Poderia simplesmente ter feito assim: 
soma_dos_quadrados += int(input(f"Digite o {i+1}º numero inteiro: ")) ** 2
'''
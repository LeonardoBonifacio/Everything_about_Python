from os import system
system('cls')

lista_de_números = [1, 2, 3, 4, 5, 6, 7, 8, 9]
produto = 1
for num in lista_de_números:
    produto *= num
print(f'O produto dessa lista de números {lista_de_números} é igual a {produto}')
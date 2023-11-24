from os import system
system('cls')

lista_numeros = []
for i in range(10):
    num = int(input('Digite qualquer número para ser armazenado em uma lista: '))
    lista_numeros.append(num)
    system('cls')

maior = max(lista_numeros)
menor = min(lista_numeros)
print(f'O maior número digitado foi {maior}')
print()
print(f'O maior número estava na posição {lista_numeros.index(maior,0,9) + 1}')
print()
print(f'O menor número digitado foi {menor}')
print()
print(f'O menor número digitado estava na posição {lista_numeros.index(menor,0,9) + 1}')


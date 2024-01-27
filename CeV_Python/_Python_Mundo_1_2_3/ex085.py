from os import system
system("cls")

numeros = [[],[]]
for num in range(7):
    numero = int(input(f'Digite o {num + 1}° valor: '))
    if(numero % 2 == 0):
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')

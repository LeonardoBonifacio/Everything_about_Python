from os import system
system('cls')

num = []

for i in range(5):
    numeros = input('Digite um número: ')
    if(numeros not in num):
        num.append(numeros)
print('O(s) número(s) digitado(s) sem  duplicatas foram: ')
for numeros in num:
    print(numeros)
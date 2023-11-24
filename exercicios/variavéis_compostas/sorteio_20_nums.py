from os import system
system('cls')
from random import randint
lista = []
acima_de_5 = 0
divisiveis_por_3 = 0
for contador in range(20):
    num = randint(1,10)
    lista.append(num)
    if(num > 5):
        acima_de_5 += 1
    if(num % 3 == 0):
        divisiveis_por_3 += 1
print(f'Aqui estão os 20 números sorteados {lista}.')
print(f'Destes 20 números {acima_de_5} estão acima de 5\n{divisiveis_por_3} são divisiveis por 3.')
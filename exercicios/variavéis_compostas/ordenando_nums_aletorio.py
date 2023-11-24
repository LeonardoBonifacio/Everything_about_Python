from os import system
system('cls')
from random import randint

vetor = []

for num in range(20):
    vetor.append(randint(0,99))
for num in vetor:
    print(f'[{num}]')
print(f'Lista ordenada: {sorted(vetor)}')
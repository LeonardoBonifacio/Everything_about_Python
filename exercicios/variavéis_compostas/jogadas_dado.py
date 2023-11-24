from os import system
from random import randint
jogadas = []
valores = [0] * 6
system('cls')
for jogada in range(100):
    jogadas.append(randint(1,6))
for jogada in jogadas:
    valores[jogada - 1] += 1
for cont in range(1,7):
    print(f'O valor {cont} foi jogado {valores[cont - 1]} vezes sendo um total de {(valores[cont - 1] / 100):.2%} das jogadas totais, que foram 100')

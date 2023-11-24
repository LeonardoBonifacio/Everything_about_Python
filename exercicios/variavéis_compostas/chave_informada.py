from os import system
system('cls')
from random import randint

inteiros = []
posicoes = []
qtd_chave = 0
for inteiro in range(30):
    inteiros.append(randint(1,15))
chave = int(input('Por favor digite um número inteiro entre 1 e 15: '))
if(chave in inteiros):
    for pos,inteiro in enumerate(inteiros):
        if(chave == inteiro):
            qtd_chave += 1
            posicoes.append(pos + 1)
    print(f'O número digitado {chave} foi encontrado {qtd_chave} vezes na minha lista e ele estava nas posições {posicoes}')
else:
    print('O número informado não foi encontrado na lista.')
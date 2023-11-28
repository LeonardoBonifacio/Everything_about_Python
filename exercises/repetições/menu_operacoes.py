'''Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida. '''
from os import system
system('cls')
while(True):
    print('-=-' * 10,'TABUADA DE OPERAÇÕES','-=-' * 10)
    op = int(input('[1] - Adição\n[2] - Subtração\n[3] - Divisão\n[4] - Multiplicação\n[0] - Sair do programa\n>>> '))
    if(op == 0):
        break
    num = int(input('Qual número deseja saber a tabuada da operação escolhida: '))
    tabuada = 0
    if(op == 1):
        while(tabuada <= 10):
            print(f'{num} + {tabuada} == {num + tabuada}')
            tabuada += 1
    elif(op == 2):
        while(tabuada <= 10):
            print(f'{num} - {tabuada} = {num - tabuada}')
            tabuada += 1
    elif(op == 3):
        tabuada = 1
        while(tabuada <= 10):
            print(f'{num} / {tabuada} = {(num / tabuada):.2f}')
            tabuada += 1
    elif(op == 4):
        while(tabuada <= 10):
            print(f'{num} x {tabuada} = {num * tabuada}')
            tabuada += 1
    input('[ENTER] - Para Continuar')
    system('cls')
print(f'Tabuada finalizada com sucesso.')


from os import system
from math import ceil
system('cls')

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número> '))
operacao = int(input('[ 1 ] - Adição\n[ 2 ] - Subtração\n[ 3 ] - Multiplicação\n[ 4 ] - Divisão\n >>>  '))

if(operacao < 1 or operacao > 4):
    print('Operação inválida')
elif(operacao == 1):
    resultado = num1 + num2
    print(f'A soma de {num1} + {num2} == {resultado}')
elif(operacao == 2):
    resultado = num1 - num2
    print(f'A subtração de {num1} - {num2} == {resultado}')
elif(operacao == 3):
    resultado = num1 * num2
    print(f'A multiplicação de {num1} x {num2} = {resultado}')
else:
    resultado = num1 / num2
    print(f'A divisão de {num1} / {num2} == {resultado} ')
if(resultado % 2 == 0):
    print('Ele é PAR')
else:
    print('Ele é IMPAR')
if(resultado > 0):
    print('Ele é POSITIVO')
else:
    print('Ele é NEGATIVO')
if(ceil(resultado) > resultado):
    print('Ele é DECIMAL')
else:
    print('Ele é INTEIRO')
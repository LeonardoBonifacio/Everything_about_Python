from os import system
system('cls')

def calcular(numA,numB,operador):
    resposta = 0
    if(operador == '+'):
        resposta = numA + numB
    elif(operador == '-'):
        resposta = numA - numB
    elif(operador == '/'):
        resposta = numA / numB
    elif(operador == '*'):
        resposta = numA * numB 
    else:
        print('Operador inválido.')
    print(f'{numA} {operador} {numB} = {resposta}')

n1 = int(input('Digite o n1: '))
print()
n2 = int(input('Digite o n2: '))
print()
op = input('Informe o operador matemático: ')

calcular(n1, n2, op)
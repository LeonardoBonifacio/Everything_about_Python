from os import system
system('cls')
historic1 = []
historicOp = []
historic2 = []
historicResult = []
count = 0
while(count != 5):
    num1 = int(input('Digite um número inteiro para calcular: '))
    historic1.append(num1)
    op = str(input('Soma -->[+]\nSubtração -->[-]\nMultiplicação -->[*]\nDivisão -->[/]\n--> ')).strip()
    historicOp.append(op)
    num2 = int(input('Digite outro número inteiro para calcular: '))
    historic2.append(num2)
    if(op == '+'):
        resultado = num1 + num2
        print(f'O resultado da soma de {num1} {op} {num2} = {resultado}')
    elif(op == '-'):
        resultado = num1 - num2
        print(f'O resultado da subtração de {num1} {op} {num2} = {resultado}')
    elif(op == '*'):
        resultado = num1 * num2
        print(f'O resultado da multiplicação de {num1} {op} {num2} = {resultado}')
    elif(op == '/'):
        resultado = num1 / num2
        print(f'O resultado da divisão de {num1} {op} {num2} = {resultado}')
    historicResult.append(resultado)
    count = count + 1
    

print('Histórico de todos o valores, operações e resultados obtidos/digitados')
print(f'Histórico dos primeiros números:\n{historic1}')
print()
print(f'Histórico das operações digitadas:\n{historicOp}')
print()
print(f'Histórico dos segundos números:\n{historic2}')
print()
print(f'Histórico dos resultados obtidos\n{historicResult}')
print()



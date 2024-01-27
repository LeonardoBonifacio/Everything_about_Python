from os import system
system('cls')

expressao = []

expressao.append(str(input('Digite uma expressão númerica com parênteses: ')))

abertos = expressao[0].count('(')
fechados = expressao[0].count(')')

if(abertos == fechados):
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta, pois o número de parênteses abertos não é igual ao número de parenteses fechados.')
'''
Jeito do guanabara
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if(simb == '('):
        pilha.append('(')
    elif(simb == ')'):
        if(len(pilha) > 0):
            pilha.pop()
        else:
            pilha.append(')')
            break
if(len(pilha) == 0):
    print('Sua expressão está correta')
else:
    print('Sua expressão não está correta.')
'''
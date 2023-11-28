from os import system
system('cls')

pilha = []
expressao = str(input('Digite uma expressão que contenha parenteses: '))

for caracter in expressao:
    if (caracter == '('):
        pilha.append(caracter)
    elif (caracter == ')'):
        if (len(pilha) > 0):
            pilha.pop()
        else:
            pilha.append(caracter)
            break
if (len(pilha) == 0):
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta.')

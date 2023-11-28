from os import system
system('cls')

inteiros = []
posicoes_10 = []
for num in range(15):
    inteiros.append(int(input(f'Digite o {num + 1}° número inteiro: ')))
for pos,inteiro in enumerate(inteiros):
    if(inteiro % 10 == 0):
        posicoes_10.append(pos + 1)
print(f'Aqui está os número informados: {inteiros}.')
if(len(posicoes_10) > 0):
    print(f'Os múltiplos de 10 se encontram na(s) posições {posicoes_10}')
else:
    print('Não houveram múltiplos de 10 digitados.')

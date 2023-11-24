from os import system
system('cls')
print('-=-' * 10,'INVERTENDO NÚMEROS INTEIROS POSITIVOS','-=-' * 10)
while(True):
    inteiro = int(input('Digite um número inteiro positivo: '))
    if(inteiro < 0):
        input('Por favor digite um número positivo, tecle [ENTER] - Para continuar...')
    else:
        break
inteiro_ao_contratrio = ''
for numero in str(inteiro)[::-1]:
    inteiro_ao_contratrio += numero
print(f'O número {inteiro} ao contrário é {inteiro_ao_contratrio}')
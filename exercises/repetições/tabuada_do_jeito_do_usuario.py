from os import system
system('cls')

print('-=-' * 10,'FAÇA A TABUADA DO SEU JEITO OO CARALHO','-=-' * 10)
tabuada = int(input('Quer a tabuada de qual valor: '))
while(True):
    comecar_por = int(input('Quer começar a tabuada de qual valor: '))
    terminar_em = int(input('Quer terminar a tabuada em qual valor: '))
    if(terminar_em < comecar_por):
        print('O número final da tabuada não pode ser menor que o inicial, por favor digite novamente...')
    else:
        break
for iteracao in range(comecar_por,terminar_em + 1):
    print(f'{tabuada} x {iteracao} = {tabuada * iteracao}')
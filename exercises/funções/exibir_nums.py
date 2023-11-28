'''def exibir_Nnums(num):
    for c in range(1,num + 1):
        print(f'{c} ' * c)

'''
def exibir_sequencia(numero):
    for numeros in range(1,numero + 1):
        print(F'{c} ',end= ' ')
    print()
        

def exibir_numero(numero):
    for numeros in range(numero + 1):
        exibir_sequencia(numeros)

num = int(input('Digite um número: '))
exibir_numero(num)

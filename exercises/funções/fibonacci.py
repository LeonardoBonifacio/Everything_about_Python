from os import system
system('cls')

def fibonacci(qtd_ele):
    termo1 = 0
    termo2 = 1
    print(termo1,end = ' >> ')
    print(termo2,end = ' >> ')
    for i in range(qtd_ele - 2):
        proximo_termo = termo1 + termo2
        print(proximo_termo,end = ' >> ')
        termo1 = termo2
        termo2 = proximo_termo
    print(' FIM')

print('Digite quantos termos da sequência fibonacci vocÊ quer ver...')
fibonacci(int(input('>> ')))
    
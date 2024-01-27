from os import system
system('cls')


def fatorial(n, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    """
    fat = 1
    string_fatorial = ''
    for c in range(1, n + 1):
        fat *= c
        if (c == n):
            string_fatorial += str(c) + ' = '
        else:
            string_fatorial += str(c) + ' x '
    string_fatorial += str(fat)

    if (show == True):
        print(string_fatorial)
    else:
        print(fat)


num = int(input('Digite que número quer saber o fatorial: '))
print('----------------------------------------------------')
fatorial(num,True)

'''
def fatorial(n, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: retorna o resultado do fatorial do número n
    """
    f = 1 
    for c in range(m,0m-1):
        if(show):
            print(c,end = ' ')
            if(c > 1):
                print(' x ',end = '')
            else:
                print(' = ',end = '')
        f *= c
    return f

#Programa principal

print(fatorial(4,show=True))
help(fatorial)

'''

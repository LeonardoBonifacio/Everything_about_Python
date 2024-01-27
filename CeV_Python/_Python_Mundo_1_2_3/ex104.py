from os import system
system('cls')

def leiaInt(msg):
    ok = False
    valor = 0
    while(True):
        n = str(input(msg))
        if(n.isnumeric() == True):
            valor = n
            ok = True
        else:
            print('\033[0;31mERRO ! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if(ok == True):
            break
    return valor

num = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {num}')








from os import system
system('cls')

def somador(n1 = 0,n2 = 0):
    s = n1 + n2
    return s
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
resp = somador(num1,num2)
print(f'A soma de {num1} + {num2} é {resp}')


def soma(arg1,arg2,arg3):
    return arg1 + arg2 + arg3

resultado = soma(1,2,3)
print(resultado)
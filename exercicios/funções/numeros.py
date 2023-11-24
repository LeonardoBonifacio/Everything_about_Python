from os import system
system('cls')

def temQuantosDigitos(numero):
    num = str(numero)
    print(f'O número {numero} têm {len(num)} digitos')

def reverterNumero(numero):
    num = str(numero)
    revertido = num[::-1]
    print(f'O reverso de {numero} é {revertido}')

n = int(input('informe um número para eu lhe dizer quantos digitos ele têm: '))
temQuantosDigitos(n)
reverterNumero(n)
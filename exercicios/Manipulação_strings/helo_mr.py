from os import system
system('cls')

nome = str(input('Digite seu primeiro nome: ')).strip().upper()

primeira_letra = nome[0]

print(f'Hello Mr:{primeira_letra}')
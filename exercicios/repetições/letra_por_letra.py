from os import system
system('cls')

nome = str(input('Digite seu nome: ')).strip().title()
print('Aqui está seu nome letra a letra. ')
for letra in (nome):
    print(letra)
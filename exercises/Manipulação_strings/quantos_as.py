from os import system
system('cls')

nome = str(input('Digite seu nome: ')).strip().upper()

print(f"A letra (A) no seu nome aparece {nome.count('A')} vezes.")
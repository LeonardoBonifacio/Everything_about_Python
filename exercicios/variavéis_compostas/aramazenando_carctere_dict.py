from os import system
system('cls')

dicionario = {}

palavra = str(input('Digite uma palavra para armazena-lá num dicionário Python: '))

for letra in palavra:
    dicionario[letra] = palavra.count(letra)

for caractere,qtd in dicionario.items():
    print(f'O caractere {caractere} foi encontrado {qtd} na palavra digitada...')
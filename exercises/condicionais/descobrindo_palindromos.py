import os
os.system('cls')

print('-----Descobrindo palíndromos-----')
palavra = input('Digite um palavra de 3 letras: ')
letra_1 = input('Digite a primeira letra dessa palavra: ')
letra_2 = input('Digite a segunda letra dessa palavra: ')
letra_3 = input('Digite a terceira letra dessa palavra: ')

if(letra_1 == letra_3):
    print(f'A palavra: {palavra} é um palíndromo.')
else:
    print(f'A palavra {palavra} não é um palíndromo.')

print('Programa finalizado com sucesso')
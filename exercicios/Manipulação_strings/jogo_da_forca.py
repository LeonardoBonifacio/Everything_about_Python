from os import system
system('cls')

import random


lista_palavras = ['leonardo', 'loucura', 'otorrinolaringologista', 'monitor', 'jabuticaba'
                  'jaca', 'deus', 'ellie', 'python', 'javascript', 'fone', 'notebook', 'manga', 'celular', 'mouse', 'garrafa', 'segunda', 'estudar', 'projeto',
                  'funções', 'celular', 'gamer', 'insalubre',' teclado']
palavra = str(random.choice(lista_palavras)).casefold().strip()

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while(True):
    senha = ''
    for letra in palavra:
        senha += (letra if letra in acertos else ' _ ')
    print(senha)
    if(senha == palavra):
        print(f'Parabens , você acertou, a palavra era {palavra}')
        break
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if(tentativa in digitadas):
        print('Você já tentou esta letra! ')
        continue
    else:
        digitadas += tentativa
        if(tentativa in palavra):
            acertos += tentativa
        else:
            erros += 1
            print('Você errou')
    print('X==:==\nX  :  ')
    print('X  O ' if erros >= 1 else 'X')
    linha2 = ['\ ','|','/']
    if(erros == 2):
        print(f"X  {linha2[1]}")
    elif(erros == 3):
        print(f"X {''.join(linha2[0:2]).replace(' ','')}")
    elif(erros >= 4):
        print(f"X {''.join(linha2).replace(' ','')}")
    linha3 = ['/','\ ']
    if(erros == 5):
        print(f"X {linha3[0]}")
    elif(erros >= 6):
        print(f"X {linha3[0]}",end = ' ')
        print(f'{linha3[1]}')
    print('X\n===========')
    if(erros == 6):
        print('Enforcado!')
        print(f'A palavra era {palavra}')
        break

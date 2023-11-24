from os import system
from random import randint
from time import sleep
system('cls')

def jogarCraps(dado,qtd_jogadas):
    global ponto
    if(dado == ponto):
        print(f'Você ganhou pois marcou novamente seu ponto -> {ponto}')
        return True
    elif(dado == 7 and ponto != 0):
        print(f'Você perdeu pois tirou um sete no  dado {dado} antes de marcar seu ponto novamente. ')
        return False
    if(qtd_jogadas == 1 and dado in [7,12]):
        print(f'Parabens você venceu pois tirou um "Natural"  que foi {dado}')
        return True
    elif(qtd_jogadas == 1 and dado in [2,3,12]):
        print(f'Que pena você perdeu meu nobre pos tirou um "Craps" que foi {dado}')
        return False
    elif(qtd_jogadas == 1 and dado in [4,5,6,8,9,10]):
        print(f'Você fez um ponto que foi ',end='')
        print(dado)
        ponto = dado
    else:
        print(f'Seu dado deu {dado}')
    
ponto = 0
c = 0
while(True):
    print('-' * 30)
    print('Vamos jogar Craps'.center(30))
    print('-' * 30)
    print('Jogando seu dado...')
    sleep(3)
    primeiro = randint(2,12)
    c += 1
    if(jogarCraps(primeiro,c) in [False,True]):
        break
    
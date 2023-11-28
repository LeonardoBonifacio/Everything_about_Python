from os import system
system('cls')
tentativas = 0
while(True):
    nome = str(input('Digite um nome com até 5 letras: '))
    if(len(nome) <= 5 ):
        print('Parabens por seguir uma ordem')
        break
    else:
        system('cls')
        print('-=-=-=-=-=Tente novamente-=-=-=-=-=\n')
        tentativas = tentativas + 1
        print(f'{tentativas} tentativas  de 3.')
        if(tentativas > 3):
            system('cls')
            break
        else:
            continue
        
from os import system
system('cls')

palavra = ''
tentativas = 0

while(palavra != 'Jaca'):
    palavra = str(input('Tente adivinhar que fruta estou pensando: \n--> ')).strip().title()
    if(palavra != 'Jaca'):
        system('cls')
        print('Errou tente denovo')
        tentativas = tentativas + 1
    else:
        print('Parabens você acertou.')
        print(f'E fez isso em {tentativas} tentativas')
    
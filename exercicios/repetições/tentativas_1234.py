from os import system
system('cls')
palavra = ''
tentativas = 0
while(palavra != '1234'):
    tentativas = tentativas + 1
    palavra = str(input('Tente adivinhar em quais 4 numeros estou pensando:\n--> '))
    if(palavra.isalpha() == True):
        print('São somente números e não letras.')
    elif(palavra == '1234'):
        print('ACERTOU')
        print(f'Fez em {tentativas} tentativas.')
from os import system
system('cls')


frase1 = str(input('Digite uma frase qualquer: '))
frase2 = str(input('Digite um trecho de frase: '))

if(frase2 in frase1):
    print(f'{frase2} está em {frase1} na posição {frase1.index(frase2)}')
else:
    print(f'{frase2} não está presente em {frase1}')
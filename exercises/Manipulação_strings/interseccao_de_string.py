from os import system
system('cls')

'''frase1 = set(input('Digite uma frase qualquer: '))
frase2 = set(input('Digite outra frase qualquer: '))
frase3 = ''.join(str(frase1.intersection(frase2)))

print(f'Caracteres iguais nas duas frases: {frase3}')'''

frase1 = str(input('Digite uma frase qualquer: '))
frase2 = str(input('Digite outra frase qualquer: '))
frase3 = ''
for caractere in frase1:
    if(caractere in frase2):
        frase3 += caractere


print(f'Caracteres iguais das duas frases: {frase3}')
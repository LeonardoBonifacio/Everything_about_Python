#Program que pede uma frase e a analisa mostrando:
#Quantas vezes aparece a letra 'a'
#Em que posição ela aparece primeiro
#Em que posição ela aparece por último
from os import system
system('cls')

frase = str(input('Digite uma frase qualquer: ').casefold().strip())

if('a' not in frase):
    print('Não existe a letra "a" na sua frase.')
else:
    vezes_A = frase.count('a')

    print(f'Nesta frase a letra "a" apareceu {vezes_A} vezes.')

    print(f'Nesta frase o "a" apareceu primeiro na posição {frase.index("a") + 1}')

    print(f'Nesta frase o "a" apareceu por ultimo na posição {frase.rindex("a") + 1}')
from os import system
system('cls')

print('-=-' * 10, 'SERA QUE ESSA FRASE É UM PALÍNDROMO ?' ,'-=-' * 10)
 
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
frase_aos_contrario = ''
for letra in frase[::-1]:
    frase_aos_contrario += letra
print(f'O inverso de {frase} é {frase_aos_contrario}')
if(frase == frase_aos_contrario):
    print('A frase digitada é um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')

'''
Jeito do guanabara(bem mais verboroso)

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = junto[::-1] PODE SER FEITO DESSE JEITO TBM SEM USAR O for
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if(inverso == junto):
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um Palíndromo')
'''
frase1 = str(input('Digite uma frase qualquer: '))
frase2 = str(input('Digite outra frase qualquer: '))
frase3 = ""
for caractere in frase1:
    if(caractere not in frase2):
        frase3 += caractere
for caractere in frase2:
    if(caractere not in frase1):
        frase3 += caractere
'''
Outra forma de resolver porém com conjuntos
frase3 = str(set(frase1) - set(frase2))
frase3 += str(set(frase2) - set(frase1))

'''

print(f'Aqui estão os caracteres únicos das 2 strings: {frase3}')
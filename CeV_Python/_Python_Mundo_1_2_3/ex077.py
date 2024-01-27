from os import system
system('cls')
print('-=-' * 10,'LSITAGEM DE VOGAIS EM PALAVRAS NA TUPLA','-=-' * 10)
palavras = ('JABUTICABA', 'OTORRINOLARINGOLOGISTA', 'ZENEFREDO', 'OBRAINDORU', 'CAPIXABA', 'JIMBROLHUDO','MASURPIAU', 'VASCO', 'NABUTICABUDO', 'GARGULHAO', 'PRIMPGADUS', 'OTOCHORANO')
cont = 0
while (True):
    if (cont == 12):
        break
    print(f'Na palavra {palavras[cont]} temos ', end='')
    for letra in palavras[cont]:
        if (letra.casefold() in 'aeiou'):
            print(letra.casefold(), end=' ')
    print('')
    cont += 1
"""
Jeito do guanabara

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ',end = '')
    for letra in palavras:
        if(letra.lower() in 'aeiou'):
            print(letra,end = ' ')
"""
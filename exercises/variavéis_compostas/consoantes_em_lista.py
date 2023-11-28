from os import system
system('cls')

while (True):
    frase = []
    frase.append(str(input(
        'Por favor digite uma frase ou palavra de 10 caracteres,(obs: espaços contam): ')))
    if (len(frase[0]) == 10):
        break
    else:
        system('cls')
print('As consoantes dessa frase foram: ',end = '')
qtd_c = 0
for c in frase[0]:
    if(c not in 'aeiouAEIOU'):
        qtd_c += 1
        print(c.upper(),end = ' ')
print(f'\nA quantidade de consoates digitadas foram: {qtd_c}')
    

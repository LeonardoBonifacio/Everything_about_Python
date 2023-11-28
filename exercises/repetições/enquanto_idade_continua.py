from os import system
system('cls')
continuar = ''
pessoa = 0
media = 0
pessoas_mais_de_21 = 0
while(continuar != 'N'):
    idade = int(input(f'Idade da {pessoa + 1}° pessoa: '))
    continuar = str(input('Continuar ? [S] ou [N] >>>')).strip().upper()
    pessoa += 1
    media += idade
    if(idade >= 21):
        pessoas_mais_de_21 += 1
media /= pessoa
print(f'Foram digitadas {pessoa} idades.')
print(f'A média da idades digitadas foi de {media}')
print(f'A quantidade de pessoas que tem mais de 21 anos é de {pessoas_mais_de_21}')
from os import system
system('cls')

media = 0
mais_de_18 = 0
menos_de_5 = 0
for pessoas in range(1,11):
    idade = int(input(f'Digite a idade da {pessoas}° pessoa: '))
    if(pessoas == 1):
        maior = idade
    else:
        if(idade > maior):
            maior = idade
    media += idade
    if(idade > 18):
        mais_de_18 += 1
    if(idade < 5):
        menos_de_5 += 1
media /= 10
print(f'A média de idade do grupo é de {media}\n{mais_de_18} pessoas tem mais de 18 anos\n{menos_de_5} pessoas tem menos de 5 anos\nA maior idade lida foi de {maior}')
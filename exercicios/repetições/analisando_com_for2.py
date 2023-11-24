from os import system
system('cls')

qtd_homens = 0
qtd_mulheres = 0
media = 0
media_homens = 0
mulheres_mais_de_20 = 0 

for pessoas in range(1,6):
    system('cls')
    idade = int(input(f'Idade da {pessoas}° pessoa: '))
    sexo = str(input(f'Sexo da {pessoas}° pessoa\n[M] - Masculino\n[F] - Feminino\n>>>   ')).strip().upper()
    if(sexo == 'M'):
        qtd_homens += 1
        media_homens += idade
    elif(sexo == 'F'):
        qtd_mulheres += 1
        if(idade > 20):
            mulheres_mais_de_20 += 1
    else:
        print('Sexo inválido')
        break
    media += idade
media /= 5
media_homens /= qtd_homens

print(f'Foram cadastrados: {qtd_homens} homens')
print(f'Foram cadastradas: {qtd_mulheres} mulheres')
print(f'A média de idade das 5 pessoas é {media}')
print(f'A média de idade dos homens é de {media_homens}')
print(f'A quantidade de mulheres que tem mais de 20 anos é {mulheres_mais_de_20}')

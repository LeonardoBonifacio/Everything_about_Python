from os import system
system('cls')
qtd_mulheres = 0
homens_mais_de_100 = 0
media_peso_mulheres = 0
for pessoa in range(1,9):
    sexo = str(input('[M]asculino ou [F]eminino >>>  ')).strip().upper()
    peso = float(input(f'Digite o {pessoa}° peso: '))
    if(sexo == 'F'):
        qtd_mulheres += 1
        media_peso_mulheres += peso
    if(sexo == 'M'):
        if(pessoa == 1):
            maior_peso_homem = peso
        else:
            if(peso > maior_peso_homem):
                maior_peso_homem = peso
        if(peso > 100):
            homens_mais_de_100 += 1
media_peso_mulheres /= qtd_mulheres
print(f'Foram cadastradas {qtd_mulheres} mulheres.')
print(f'{homens_mais_de_100} homens pesam mais de 100kg')
print(f'A média de peso entre as mulheres foi de {media_peso_mulheres}')
print(f'O maior peso entre os homens foi de {maior_peso_homem}')
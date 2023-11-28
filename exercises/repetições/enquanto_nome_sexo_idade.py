from os import system
system('cls')
continuar = ''
qtd_pessoas = 0
qtd_mulheres = 0
media_idade_grupo = 0
homens_mais_de_30 = 0
mulheres_menos_18 = 0
while(continuar != 'N'):
    system('cls')
    print('====== ANALISANDO UMAS COISA AI ======')
    qtd_pessoas += 1
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('[M]asculino\n[F]eminino\n>>>  ')).strip().upper()
    continuar = str(input('Continuar? [S] ou [N] >>> ')).upper().strip()
    if(qtd_pessoas == 1):
        nome_pessoa_mais_velha = nome
        maior_idade = idade
    else:
        if(idade > maior_idade):
            nome_pessoa_mais_velha = nome
    if(sexo == 'F'):
        qtd_mulheres += 1
        if(idade < 18):
            mulheres_menos_18 += 1
        if(qtd_mulheres == 1):
            nome_da_mulher_mais_jovem = nome
            menor_idade_mulher = idade
        else:
            if(idade < menor_idade_mulher):
                nome_da_mulhere_mais_jovem = nome
    if(sexo == 'M'):
        if(idade > 30):
            homens_mais_de_30 += 1
    media_idade_grupo += idade
media_idade_grupo /= qtd_pessoas

print(f'O nome da pessoa mais velha é {nome_pessoa_mais_velha}')
if(qtd_mulheres > 0):
    print(f'O nome da mulher mais jovem é {nome_da_mulher_mais_jovem}')
    print(f'A quantidade mulheres que tem menos de 18 é {mulheres_menos_18}')
print(f'A média de idade do grupo é de {media_idade_grupo}')
print(f'A quantidade de homens que têm mais de 30 anos é {homens_mais_de_30}')


from os import system
system('cls')

mulheres_menos_20_anos = 0
media = 0
maior_idade_homem = 0
cont_homens = 0
cont_mulheres = 0
for i in range(1,5):
    print(f'----- {i}° PESSOA -----')
    sexo = int(input('[1] - Homem\n[2] - Mulher\n>>>  '))
    nome = str(input('Digite seu primeiro nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    media += idade
    if(sexo == 1):
        cont_homens += 1
        if(idade > maior_idade_homem):
            maior_idade_homem = idade
            nome_do_homem_mais_velho = nome
    elif(sexo == 2):
        cont_mulheres += 1
        if(idade < 20):
            mulheres_menos_20_anos += 1
    system('cls')
media /= 4
print(f'A média das idades lidas foi de \033[1m{media}\033[m')
if(cont_homens > 0):
    print(f'O nome do homem mais velho é \033[1m{nome_do_homem_mais_velho}\033[m e ele tem \033[1m{maior_idade_homem}\033[m anos.')
print(f'\033[1m{mulheres_menos_20_anos}\033[m mulheres têm menos de 20 anos.')
print(f'Foram informados \033[1m{cont_homens}\033[m homens e \033[1m{cont_mulheres}\033[m mulheres.')
from os import system
system('cls')
continuar = ''
qtd_homens = 0
media_homens = 0
pessoas = 1
qtd_mulheres = 0
print('ANALISANDO POR SEXO E IDADE')
while(continuar != 'N'):
    sexo = str(input('[M]asculino\n[F]eminino\n>>> ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    continuar = str(input('Continuar? [S] ou [N] >>> ')).strip().upper()
    if(pessoas == 1):
        maior_idade = idade
    if(sexo == 'M'):
        qtd_homens += 1
        media_homens += idade
    if(sexo == 'F'):
        qtd_mulheres += 1
        if(qtd_mulheres == 1):
            menor_idade_mulher = idade
        if(idade < menor_idade_mulher):
            menor_idade_mulher = idade
    if(idade > maior_idade):
        maior_idade = idade
    pessoas += 1
print(f'A maior idade lida foi {maior_idade} anos')
if(qtd_homens > 0):
    media_homens /= qtd_homens
    print(f'Foram cadastrados {qtd_homens} homens')
    print(f'A média de idade entre os homens é de {media_homens:.2f} .')
if(menor_idade_mulher > 0):
    print(f'A idade da mulher mais jovem informada foi de {menor_idade_mulher} anos')
if(qtd_mulheres > 0):
    print(f'Foram cadastradas {qtd_mulheres} mulheres.')

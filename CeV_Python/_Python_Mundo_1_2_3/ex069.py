from os import system
system('cls')

mulheres_com_menos_de_20 = qtd_homens = qtd_adultos = 0
while(True):
    system('cls')
    print('-=-' * 6,'CADASTRANDO PESSOAS','-=-' * 6)
    while(True):
        idade = int(input('Quantos anos essa pessoas tem? >> '))
        if(idade < 0):
            print('Idade inválida')
            input('[ENTER] - Para Continuar')
        else:
            break
    while(True):
        sexo = str(input('Qual o sexo dessa pessoa? [M]asculino ou [F]eminino:  ')).strip().upper()[0]
        if(sexo != 'F' and sexo != 'M'):
            print('Sexo inválido')
            input('[ENTER] - Para Continuar')
        else:
            break
    if(idade >= 18):
        qtd_adultos += 1
    if(sexo == 'M'):
        qtd_homens += 1
    if(sexo == 'F' and idade < 20):
        mulheres_com_menos_de_20 += 1
    while(True):
        continuar = str(input('Deseja continuar cadastrando pessoas? [S]im ou [N]ão:  ')).strip().upper()[0]
        if(continuar != 'S' and continuar != 'N'):
            print('Valor inválido')
        else:
            break
    if(continuar == 'N'):
        break
system('cls')
print('-=-' * 10,'INÍCIO DO RELATÓRIO','-=-' * 10)
print(f'Foram cadastrados {qtd_adultos} pessoas com mais de 18 anos')
print(f'Ao menos {qtd_homens} homem(ns) foi cadastrado')
print(f'{mulheres_com_menos_de_20} mulher(es) com menos de 20 anos foram cadastradas')
print('-=-' * 10,'FINAL DO RELATÓRIO','-=-' * 10)
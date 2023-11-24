from os import system
system('cls')
qtd_pessoas = 0
while(True):
    print('-=-' * 10, 'VALIDANDO INFORMAÇÕES', '-=-' * 10)
    while(True):
        sexo = str(input('Sexo:[F]eminino [M]asculino\n>>> ')).strip().upper()[0]
        if(sexo == 'M' or sexo == 'F'):
            break
        print('Sexo inválido')
    while(True):
        nome = str(input('Digite seu nome: ')).strip().title()
        if(len(nome) >= 2):
            break
        print('Seu nome precisa conter mais que 3 caracteres')
    while(True):
        idade = int(input('Digite sua idade: '))
        if(idade > 0 and idade < 150):
            break
        print('Você informou uma idade inválida')
    while(True):
        salario = float(input('Seu salário R$'))
        if(salario > 0):
            break
        print('Informe um valor maior que 0 para o salário')
    while(True):
        estado_civil = str(input('Estado civil [S]olteiro(a) [C]asado(a) [V]iúvo(a) [D]isvorciado(a)\n>>> ')).strip().upper()[0]
        if(estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D'):
            break
        print('Estado civil inválido.')
    continuar = str(input('Cadastrar mais pessoas?\n[S]im\n[N]ão\n>>> ')).strip().upper()[0]
    qtd_pessoas += 1
    system('cls')
    if(continuar == 'N'):
        break
print(f'Cadastro finalizado com sucesso,foram cadastrados {qtd_pessoas} pessoas.')
        

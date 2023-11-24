from os import system
system('cls')

nome_funcionario = input('Nome do funcionário: ')
salario_funcionario = float(input('Salário funcionário: '))
anos_trabalha_empresa = float(input('Anos que trabalha na empresa: '))

if(anos_trabalha_empresa <= 3.0):
    print(f'Parabens {nome_funcionario} , você ganhou um aumento de 3%')
    novo_salario = salario_funcionario + (salario_funcionario * (3/100))
    print(f'Seu novo salário é de {novo_salario}')
elif(anos_trabalha_empresa > 3.0 and anos_trabalha_empresa <= 10.0):
    print(f'Parabens {nome_funcionario} , você ganhou um aumento de 12.5%')
    novo_salario = salario_funcionario + (salario_funcionario * (12.5/100))
    print(f'Seu novo salário é de {novo_salario}')
else:
    print(f'Parabens {nome_funcionario} , você ganhou um aumento de 20%')
    novo_salario = salario_funcionario + (salario_funcionario * (20/100))
    print(f'Seu novo salário é de {novo_salario}')
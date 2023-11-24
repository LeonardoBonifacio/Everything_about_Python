from os import system
system('cls')

print('----------REAJUSTANDO SALÁRIOS----------')

salario_atual = float(input('Digite seu salario atual R$'))
anos_na_empresa = int(input('Há quantos anos você trabalha na empresa: '))
genero = int(input('[1] - Homem\n[2] - Mulher\n-> '))

if(anos_na_empresa > 0):
    if(genero == 2):
        if(anos_na_empresa < 15):
            aumento = salario_atual + (salario_atual * (5/100))
            print(f'Por trabalhar a {anos_na_empresa} anos e ser mulher seu novo salário será de R${aumento:.2f}')
        elif(anos_na_empresa >= 15 and anos_na_empresa <= 20):
            aumento = salario_atual + (salario_atual * (12/100))
            print(f'Por trabalhar a {anos_na_empresa} anos e ser mulher seu novo salário será de R${aumento:.2f}')
        elif(anos_na_empresa > 20):
            aumento = salario_atual + (salario_atual * (23/100))
            print(f'Por trabalhar a {anos_na_empresa} anos e ser mulher seu novo salário será de R${aumento:.2f}')
    elif(genero == 1):
        if(anos_na_empresa < 20):
            aumento = salario_atual + (salario_atual * (3/100))
            print(f'Por trabalhar a {anos_na_empresa} anos e ser homem seu novo salário será de R${aumento:.2f}')
        elif(anos_na_empresa >= 20 and anos_na_empresa <= 30):
            aumento = salario_atual + (salario_atual * (13/100))
            print(f'Por trabalhar a {anos_na_empresa} anos e ser homem seu novo salário será de R${aumento:.2f}')
        elif(anos_na_empresa > 30):
            aumento = salario_atual + (salario_atual * (25/100))
            print(f'Por trabalhar a {anos_na_empresa} anos e ser homem seu novo salário será de R${aumento:.2f}')
    else:
        print('Você não digitou um valor válido.')
else:
    print('Você não trabalha na nossa empresa ou digitou um valor abaixo de 0.')
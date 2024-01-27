from os import system
system('cls')

print('-----CALCULANDO AUMENTOS-----')

salario = float(input('Digite seu salário R$'))

if(salario <= 1250.00):
    aumento = salario + (salario * (15/100))
    print(f'Parabens você ganhou um aumento de 15%\nSeu novo salário é de R${aumento:.2f}')
else:
    aumento = salario + (salario * (10/100))
    print(f'Parabens você ganhou um aumento de 10%\nSeu novo salário é de R${aumento:.2f}')

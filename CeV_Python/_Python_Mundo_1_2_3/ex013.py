from os import system
system('cls')

salario = float(input('Digite o seu salário atual R$'))
aumento = salario * (15/100)
novo_salario = salario + aumento

print(f'Parabens você recebeu um aumento de R${aumento:.2f} e seu novo salário no mês que vem será de R${novo_salario:.2f}')
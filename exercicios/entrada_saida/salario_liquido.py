'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para imposto de renda, 8% para INSS e 5% para o sindicato , faça um programa que nos dê: salario bruto, quanto pagou ao INSS, quanto apgou ao sindicato, salário liquido.
+ Salário Bruto: R$
- IR(11% ): R$
- INSS (8%): R$
- Sindicato(5%); R$
= Salário liquido: R$

Obs:Salário bruto - descontos = Salário liquido.
'''
import os
os.system('cls')

ganha_por_hora = int(input('Quanto você ganha por hora: '))
horas_trabalhadas_no_mes = int(input('Quantas horas você trabalha por mês: '))
salario_bruto = ganha_por_hora * horas_trabalhadas_no_mes
imposto_renda = 11/100 * salario_bruto
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
descontos = imposto_renda + inss + sindicato  

print(f'Salário bruto: R${salario_bruto:.2f}.')
print(f'Pagou: R${imposto_renda:.2f} ao imposto de renda.')
print(f'Pagou: R${inss:.2f} ao INSS.')
print(f'Pagou: R${sindicato:.2f} ao sindicato.')
print(f'Seu salario liquido foi de R${salario_bruto - descontos}.')

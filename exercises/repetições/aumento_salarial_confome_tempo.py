from os import system
system('cls')

print('-=-' * 10,'CONCEDENDO AUMENTOS ANUAIS','-=-' * 10)

salario_inicial = float(input('Qual era o seu salário inicial em 1995 quando comeceu a trabalhar ? R$'))
aumentos = 1.5
novo_salario = salario_inicial + (salario_inicial * (aumentos/100))
ano = 1995
ano_atual = int(input('Em que ano estamos? '))
print(f'O antigo salário desse funcionário me 1996 era R${novo_salario:.2f}')
for anos in range(ano_atual - ano):
    novo_salario += (novo_salario * (aumentos/100))
    aumentos *= 2
print(f'Apos {ano_atual - ano} anos o salário desse funcionário aumentou e passou a ser R${novo_salario:.2f}')
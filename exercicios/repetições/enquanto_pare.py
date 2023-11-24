'''Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite O (zero). l o final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética. '''
from os import system
system('cls')
media = soma = qtd_num = 0
while(True):
    num = int(input(f'Digite o {qtd_num + 1}° número(0 for stop): '))
    if(num == 0):
        break
    qtd_num += 1
    soma += num
media = soma / qtd_num
print(f'Você digitou {qtd_num} números.')
print(f'A soma desses números é {soma}.')
print(f'E a média aritmética entre eles é de {media:.2f}')
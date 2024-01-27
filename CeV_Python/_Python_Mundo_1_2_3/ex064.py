from os import system
system('cls')
qtd = num = soma = 0
while(num != 999):
    num = int(input('Digite um número ou [999 para encerrar]: '))
    if(num == 999):
        pass
    else:
        qtd += 1
        soma += num
print(f'Você digitou {qtd} números e a soma entre eles é de {soma} ')

'''
qtd = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while(num != 999):
    soma += num
    qtd += 1
    num = int(input('Digite um número [999 para parar]: ))
print(f'Você digitou {qtd} números e a soma entre eles é de {soma}')

Fazendo com que o número seja lido antes da repetição e ao final dela, eliminamos a condição que testava se o número lido era 999, pois ao digitar 999 antes da repetição o programa ja é finalizado e ao digitar no final o programa também é finalizado e o 999 não é atribuido a [qtd] e nem a [soma].
'''
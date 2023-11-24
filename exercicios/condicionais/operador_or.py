from os import system
system('cls')

idade = int(input('Digite sua idade: '))

condicao = int(input('[1] - Saúdavel\n[2] - Inválido\n-> '))

if(idade >= 65 or condicao == 2):
    print('Pode aposentar')
else:
    print('Ainda não pode aposentar')
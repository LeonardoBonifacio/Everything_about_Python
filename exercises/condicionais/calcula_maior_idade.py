'''
Programa que le o ano de nascimento do usuário e mostra se em dezembro desse ano ele será maior ou menor de idade
'''
import os 
os.system('cls')

ano_nasc = int(input('Que ano você nasceu: '))
ano_atual = 2023
idade = ano_atual - ano_nasc

if(idade >=18):
    print('Você é maior de idade.')
    print('Você pode se cadastrar no nosso sistema.')
else:
    print('Você é menor de idade.')
    print('Você não pode se cadastrar no nosso site!')
    print('Tente novamente quando fizer 18 anos!')
    print('Obrigado pelo interesse no nosso sistema.')
    
print('Programa finalizado com sucesso.')
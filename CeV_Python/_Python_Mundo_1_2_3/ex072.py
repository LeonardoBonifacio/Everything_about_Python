from os import system
system('cls')
contagem_extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while(True):
    print('-=-' * 10,'CONTAGEM POR EXTENSO','-=-' * 10)
    while(True):
        num = int(input('Digite um número entre 0 e 20 para ver uma contagem por extenso:  '))
        if(num  < 0 or num > 20):
            print('Por favor digite um número maior que 0 e menor que 20...')
        else:
            break
    print(f'Você digitou o número: {contagem_extenso[num]}\nE aqui está uma contagem de 0 até ele por extenso...')
    for num_cont in range(0,num + 1):
        if(num_cont == num):
            print(contagem_extenso[num_cont],end = '.')
        else:
            print(contagem_extenso[num_cont],end = ', ')
    continuar = str(input('\nVocê quer continuar? [S]im ou [N]ão ')).upper().strip()[0]
    if(continuar == 'N'):
        break
    system('cls')
print('Contagem finalizada com sucesso...')
print('Não volte sempre...')
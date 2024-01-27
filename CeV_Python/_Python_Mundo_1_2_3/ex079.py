from os import system
system('cls')

lista_numeros = []

while(True):
    print('-=-' * 10,'ADICIONANDO VALORES EM UMA LISTA','-=-' * 10)
    num = int(input('Digite qualquer número inteiro: '))
    if(num not in lista_numeros):
        lista_numeros.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar')
    continuar = str(input('Continuar a digitar novos valores [S]im ou [N]ão ')).strip().upper()[0]
    if(continuar == 'N'):
        break
    system('cls')
lista_numeros.sort()
print('-=-' * 15)
print(f'Você digitou os valores:{lista_numeros}')
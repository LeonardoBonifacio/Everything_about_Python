from os import system
system('cls')

lista_numeros = []
while(True):
    print('-=-' * 10,'ARMAZENANDO VALORES EM UMA LISTA','-=-' * 10)
    lista_numeros.append(int(input('Digite qualquer número inteiro para preencher uma lista: ')))
    continuar = str(input('Quer adicionar mais valores? [S]im ou [N]ão >>>')).strip().upper()[0]
    if(continuar == 'N'):
        break
    system('cls')
print(f'A)Foram armazenados: {len(lista_numeros)} valores.')
print(f'B)Aqui está os valores armazenados: {lista_numeros}.')
lista_numeros.sort(reverse = True)
print(f'C)Aqui está os valores de forma descrescente: {lista_numeros}.')
if(5 in lista_numeros):
    posicoes = []
    for pos,numero in enumerate(lista_numeros):
        if(numero == 5):
            posicoes.append(pos + 1)
    print(f'D)O valor 5 foi digitado e está armazenado na lista, nas posições {posicoes}')
else:
    print(f'D)O valor 5 não foi digitado, logo ele não está na lista.')

from os import system
system('cls')

pessoa = {}
lista_de_pessoas = list()
media = 0
while(True):
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome da pessoa: '))
    while(True):
        pessoa['Sexo'] = str(input('Sexo da pessoa: [M/F]')).strip().upper()[0]
        if(pessoa['Sexo'] not in 'MF'):
            print('ERRO! Por favor, digite apenas M ou F.')
            del pessoa['Sexo']
        else:
            break
    pessoa['Idade'] = int(input('Idade da pessoa: '))
    media += pessoa['Idade']
    lista_de_pessoas.append(pessoa.copy())
    while(True):
        continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
        if(continuar not in 'SN'):
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    if(continuar == 'N'):
        break
print('-=-' * 30)
print(f'A) O grupo tem {len(lista_de_pessoas)} pessoas.')
print(f'B) A média de idade é de {media/len(lista_de_pessoas):5.2f} anos')
print('C) As mulheres cadastradas foram: ', end = '')
for pessoa in lista_de_pessoas:
    if(pessoa['Sexo'] == 'F'):
        print(pessoa['Nome'],end = ' ')
print('\nD)Lista das pessoas que estão acima da média: ')
for pessoa in lista_de_pessoas:
    if(pessoa['Idade'] > media/len(lista_de_pessoas)):
        for k,v in pessoa.items():
            print(f'    {k} = {v}; ',end = ' ')
        print()
print('<< ENCERRADO >> ')
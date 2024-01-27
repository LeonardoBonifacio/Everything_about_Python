from os import system
system('cls')

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste.copy())
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste.copy())
print(galera)

galera = [['João',19], ['Ana', 22], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado.copy())
    dado.clear()
print(galera)

for pessoa in galera:
    if(pessoa[1] >= 21):
        print(f'{pessoa[0]} é maior da idade.')
        totmai += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')
from os import system
system('cls')

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

n_termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
for i in range(10):
    print(f'{n_termo} -> ',end = '')
    n_termo += razao
print('ACABOU')

'''
Posso fazer assim tbm: 

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro,decimo + razao , razao):
    print(c,end = '')
print('ACABOU')
'''
from os import system
system('cls')

# Dicionários

# dicionario = {}  ou dicionario = dict()

pessoas = {'nome': 'Leonardo', 'sexo': 'Masculino', 'idade': 19}

print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo'])
print()
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())
print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()
for keys in pessoas.keys():
    print(keys)
print()
for values in pessoas.values():
    print(values)
print()
for k,v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['sexo']
pessoas['nome'] = 'Bonifácio'
pessoas['peso'] = 70
pessoas['Cursando'] = 'ADS'
print(pessoas.items())

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

print(brasil[0]['sigla'])

print(brasil[1]['uf'])

print(brasil[0]['uf'])


estado = {}
brasil = []

for c in range(3):
    estado['uf'] = str(input('Digite o nome do estado: '))
    estado['sigla'] = str(input('Digite a sigla desse estado: '))
    brasil.append(estado.copy())

print(brasil)
for e in brasil:
    for k,v in e.items():# ou .keys() ou .values()
        print(f'O campo {k} tem valor {v}')

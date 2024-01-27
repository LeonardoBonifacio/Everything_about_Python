from os import system
system('cls')

tabela_brasileirao = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'Internacional', 'Bragantino', 'Fortaleza', 'Atlético-Paranaense', 'Atlético-Mineiro', 'São Paulo', 'Cruzeiro', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás', 'Vasco da gama', 'América', 'Coritiba')

print('-=-' * 10,'ANÁLISE DO BRASILEIRÃO EM JULHO DE 2023','-=-' * 10)
print(f'Lista de times do Brasileirão: \n{tabela_brasileirao}')
print()
print(f'B)Os cinco primeiros colocados da tabela são:')#poderia ter mostrado com tabela_brasileirao[:5]
for colocados in range(5):
    print(tabela_brasileirao[colocados])
print()
print(f'C)Os quatro últimos colocados da tabela são: ')
for colocados in tabela_brasileirao[16:]:#poderia ter feito assim: tabela_brasileirao[-4:]
    print(colocados)
print()
print(f'D)Aqui está os times em ordem alfábética:\n{sorted(tabela_brasileirao)}.')
print()
if('Chapecoense' in tabela_brasileirao):
    print(f'E)O Chapecoense está na posicão {tabela_brasileirao.index("Chapecoense") + 1}° do Brasileirão')
else:
    print('E)O Chapecoense não se encontra na tabela dos 20° primeiros colocados do Brasileirão.')
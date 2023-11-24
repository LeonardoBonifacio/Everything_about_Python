from os import system
system('cls')
nomes = []
idades = []
for pessoas in range(9):
    nomes.append(str(input(f'Digite o nome da {pessoas + 1}° pessoa: ')))
    idades.append(int(input(f'Digite a idade da {pessoas + 1}° pessoa: ')))
print('Listagem abaixo das pessoa menores de 18 anos')
for pos,idade in enumerate(idades):
    if(idade < 18):
        print(nomes[pos],' com ',idade,'anos')
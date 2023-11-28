from os import system
system("cls")

Idades = []
Alturas = []
media_altura = 0
alunos_baixos_acima_13 = 0
print('-=-' * 10,'TRATANDO IDADES E ALTURAS COM LISTAS','-=-' * 10)
for aluno in range(30):
    Idades.append(int(input(f'Digite a idade do {aluno + 1}° aluno: ')))
    Alturas.append(float(input(f'Digite a altura do {aluno + 1}° aluno: ')))
    media_altura += Alturas[aluno]
media_altura /= 30
for pos,idade in enumerate(Idades):
    if(idade > 13 and Alturas[pos] < media_altura):
        alunos_baixos_acima_13 += 1
print(f'{alunos_baixos_acima_13} alunos com mais de 13 anos possuem altura inferior a média de altura({media_altura:.2f}m) de todos os alunos.')

for idade,altura in zip(Idades,Alturas):
    print(idade,altura)
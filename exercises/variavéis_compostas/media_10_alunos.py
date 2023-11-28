from os import system
system('cls')

media_alunos = []
media_maior_igual_a_7 = 0
for alunos in range(10):
    media = []
    print(f'Digite as 4 notas do {alunos + 1}° aluno.')
    for nota in range(1,5):
        media.append(float(input(f'Digite a {nota}° nota: ')))
    media_alunos.append(sum(media)/4)
    if(media_alunos[alunos] >= 7):
        media_maior_igual_a_7 += 1

print(f'O número de alunos com média maior ou igual a 7 foi: {media_maior_igual_a_7}')

for alunos in range(10):
    print(f'A média do {alunos + 1}° aluno foi {media_alunos[alunos]:.2f}.')


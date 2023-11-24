from os import system
system('cls')
aluno = 0
media_idade = 0
idade = 0
while(idade != 999):
    system('cls')
    print('Digite 999 na idade para encerrar o programa.')
    idade = int(input(f'Idade do {aluno + 1}° aluno: '))
    if(idade == 999):
        pass
    else:
        media_idade += idade
        aluno += 1
media_idade /= aluno
print(f'Extistem {aluno} alunos  nessa turma')
print(f'A média de idade dessa turma é de {media_idade}.')
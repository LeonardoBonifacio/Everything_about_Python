from os import system
system('cls')

print('-=-' * 10,'CALCULANDO A MÉDIA DE ALUNOS POR TURMA','-=-' * 10)

qtd_turmas = int(input('Existem quantas turmas nessa faculdade? '))
media_alunos = 0
for turmas in range(qtd_turmas):
    while(True):
        qtd_alunos_por_turma = int(input(f'Quantos alunos na {turmas}° Turma? '))
        if(qtd_alunos_por_turma > 40):
            print('Uma turma deve ser no máximo 40 alunos, por favor mova uma parte desses alunos para outra turma.')
        else:
            media_alunos += qtd_alunos_por_turma
            break
media_alunos /= qtd_turmas
print(f'Nessas {qtd_turmas} turmas a média de alunos em cada uma delas foi de {media_alunos:.2f}')
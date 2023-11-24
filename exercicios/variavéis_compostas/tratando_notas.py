from os import system
system('cls')
posicoes = []
notas = []
acima_media = 0
for nota in range(10):
    notas.append(float(input(f'Digite a nota do {nota + 1}° aluno: ')))
print(f'A)A média de notas da turma é de {sum(notas)/10:.2f}')
for pos,nota in enumerate(notas):
    if(nota > sum(notas)/10):
        acima_media += 1
    if(nota == max(notas)):
        posicoes.append(pos + 1)
print(f'B){acima_media} alunos estão acima da média de notas da turma.')
print(f'C)A maior nota informada foi {max(notas)}')
print(f'D)A maior nota aparece no(s) índice(s): {posicoes}')
print(f'E)Aqui está todas as notas informadas: ')
for pos,nota in enumerate(notas):
    print(f'{pos+ 1}° {nota:.2f}')
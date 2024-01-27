from os import system
system('cls')

alunos = []
nome = []
nota = []
while(True):
    nome.append(str(input('Digite o nome do aluno: ')))
    nota.append(float(input('Digite a 1° nota desse aluno: ')))
    nota.append(float(input('Digite a 2° nota desse aluno: ')))
    nome.extend([nota.copy(),sum(nota)/2])
    nota.clear()
    alunos.append(nome.copy())
    nome.clear()
    resp = str(input('Deseja continuar informando alunos e notas? [S/N]')).strip().upper()[0]
    if(resp == 'N'):
        break
print(f"{'No.':<5}{'NOME':<10}{'MÉDIA':<15}")
for pos,aluno in enumerate(alunos):
    print(f'{pos:<5}{aluno[0]:<10}{aluno[2]:<15}')
while(True):
    pos = int(input('Mostrar notas de qual alunos? (999 interompe)'))
    if(pos == 999):
        break
    elif(pos < 0 or pos > len(alunos)):
        print(f'Por favor digite um valor correspondente com a tabela acima.')
    else:
        print(f'Notas de {alunos[pos][0]} são {alunos[pos][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SMEPRE >>>')


#Solução do guanabara

'''
ficha = list()

while(True):
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if(resp in 'Nn'):
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumrate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while(True):
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if(opc == 999):
        print('FINALIZANDO...')
        break
    if(opc <= len(ficha) - 1):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

'''













'''alun = str(input('Por favor digite exatamente o nome do aluno que deseja saber as notas separadamente ou pressione [ENTER] para encerrar o programa.'))
for aluno in alunos:
    if(alun == aluno[0]):
        print(f'Notas: {aluno[1]}')
'''
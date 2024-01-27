from os import system
system('cls')

aluno = {}

while(len(aluno) < 3):
    aluno['Nome'] = str(input('Digite o nome do aluno: '))
    aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
    if(aluno['Média'] >= 7):
        aluno['Situação'] = 'Aprovado'
    
    elif(aluno['Média'] >= 5):
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
print('-=-' * 30)
for k,v in aluno.items():
    print(f'    - {k} é igual a {v}')
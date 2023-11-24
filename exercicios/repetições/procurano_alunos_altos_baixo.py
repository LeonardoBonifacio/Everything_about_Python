from os import system
system('cls')

for alunos in range(1,11):
    while (True):
        numero_do_aluno = int(input('Digite o código de 3 números do aluno: '))
        if (len(str(numero_do_aluno)) != 3):
            print('Eu disse um código de 3 números...')
        else:
            break
    altura_do_aluno = float(input(f'Digite a altura do {alunos}° aluno [ex 1.75]: '))
    if (alunos == 1):
        mais_alto = altura_do_aluno
        codigo_mais_alto = numero_do_aluno
        mais_baixo = altura_do_aluno
        codigo_mais_baixo = numero_do_aluno
    else:
        if (altura_do_aluno > mais_alto):
            mais_alto = altura_do_aluno
            codigo_mais_alto = numero_do_aluno
        if (altura_do_aluno < mais_baixo):
            mais_baixo = altura_do_aluno
            codigo_mais_baixo = numero_do_aluno
print(f'O aluno de código {codigo_mais_alto} é o alunos mais alto com {mais_alto}m de todos os {alunos} informados.\nO aluno de código {codigo_mais_baixo} é o aluno mais baixo com {mais_baixo}m de todos os {alunos} informados.')


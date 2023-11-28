from os import system
system('cls')
acertos_list = []
alunos_list = []
qtd_alunos = media = 0
gabarito = []
print('-=-' * 10,'RESPOSTAS','-=-' * 10)
for resp in range(1,11):
    while(True):
        gabarito.append(input(f'Professor digite a resposta da {resp}° questão: '))
        if(gabarito[resp -1] not in 'ABCDEabcde'):
            print('Poxa professor o senhor mesmo sabe que as resposta são [A/B/C/D/E],tecla [ENTER] ai e tenta denovo namoral...')
            gabarito.pop()
        else:
            break
system('cls')
while(True):
    acertos = 0
    print('-=-' * 10,'A PROVA DE TUDO','-=-' * 10)
    aluno = str(input('Nome do aluno: '))
    for questoes in range(1,11):
        while(True):
            resposta = str(input(f'{questoes}° questão [A/B/C/D/E]: ')).strip().upper()[0]
            if(resposta not in 'ABCDE'):
                input('As opções para resposta são [A/B/C/D/E]\n[ENTER] para tentar novamente...')
                system('cls')
            else:
                break
        if(questoes == 1 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 2 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 3 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 4 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 5 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 6 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 7 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 8 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 9 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
        if(questoes == 10 and resposta == str(gabarito[questoes - 1]).upper()):
            acertos += 1
    qtd_alunos += 1
    media += acertos
    alunos_list.append(aluno)
    acertos_list.append(acertos)
    outro_aluno = str(input('Digite [0] para encerrar a prova ou tecle [ENTER] caso outro aluno queira fazer a prova >>> ')).strip()
    if(outro_aluno == '0'):
        break
    system('cls')
maior = -1
menor = 11
for nota in acertos_list:
    if(nota > maior):
        maior = nota
    if(nota < menor):
        menor = nota
pos_maior = acertos_list.index(maior)        
pos_menor = acertos_list.index(menor)
system('cls')
print(f'Ao todo {qtd_alunos} alunos fizeram a prova utilizando esse sistema.')
print(f'A média de nota da Turma foi de {media/qtd_alunos:.2f}')
print(f'A maior nota foi {maior} e foi do aluno: {alunos_list[pos_maior]}\nA menor nota foi {menor} e foi do aluno: {alunos_list[pos_menor]}')
from os import system
system('cls')
eleitores_baptista = eleitores_defante = eleitores_miranda = eleitores_calango = eleitores_nilce = eleitores_brancos = eleitores_nulos = 0
while(True):
    print('-=-' * 10,'ELEIÇÃO PARA O LADRÃO','-=-' * 10)
    while(True):
        voto = int(input('Vai votar em quem ?\n[1] - Diogo Defante\n[2] - João Miranda\n[3] - Baptista\n[4] - Calango\n[5] - Nilce Moreto\n[6] - Voto Nulo\n[7] - Voto em Branco\n>>>  '))
        if(voto not in [1, 2, 3, 4, 5, 6, 7]):
            print('Por favor digite um voto válido,[1 a 7]...')
        else:
            break
    if(voto == 1):
        eleitores_defante += 1
    elif(voto == 2):
        eleitores_miranda += 1
    elif(voto == 3):
        eleitores_baptista += 1
    elif(voto == 4):
        eleitores_calango += 1
    elif(voto == 5):
        eleitores_nilce += 1
    elif(voto == 6):
        eleitores_brancos += 1
    elif(voto == 7):
        eleitores_nulos += 1
    votar_mais = (input('Digite [0] para para de votar ou [ENTER] para votar novamente >>> '))
    system('cls')
    if(votar_mais == '0'):
        break
print(f'O candidato Defante  teve {eleitores_defante} votos\nO candidato Miranda teve {eleitores_miranda} votos\nO candidato Baptista teve {eleitores_baptista} votos\nO candidato Calango teve {eleitores_calango} votos\nA candidata Nilce teve {eleitores_nilce} votos\nForam contabilizados {eleitores_brancos} votos brancos\nForam contabilizados {eleitores_nulos} votos nulos.')

tot_votos = eleitores_defante + eleitores_miranda + eleitores_baptista + eleitores_calango + eleitores_nilce + eleitores_brancos + eleitores_nulos
print(f'O percentual de votos nulos sobre o total de votos foi de {((eleitores_nulos / tot_votos) * 100):.2f}%\nO percentual de votos brancos sobre o total de votos foi de {((eleitores_brancos/tot_votos) * 100):.2f}%')


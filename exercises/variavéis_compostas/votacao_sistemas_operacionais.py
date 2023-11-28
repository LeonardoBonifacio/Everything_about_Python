from os import system
votos = [0] * 6
sistemas = ['Windows', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outros']
while(True):
    system('cls')
    print('-=-' * 10,'BRIGUINHA ENTRE SISTEMAS OPERACIONAIS','-=-' * 10)
    print('-=-' * 10,' QUAL O MELHOR SISTEMA OPERACIONAL ?','-=-' * 10)
    sistema = int(input('[1] - Windows\n[2] - Unix\n[3] - Linux\n[4] - Netware\n[5] - Mac OS\n[6] - Outros\n[0] - Encerrar a votação\n>>> '))
    if(sistema not in range(0,7)):
        print('Valor inválido para votação, por favor tente novamente...')
    else:
        if(sistema == 0):
            break
        else:
            input('Voto computado com sucesso...[ENTER]')
            votos[sistema - 1] += 1
print(f'Tivemos um total de {sum(votos)} votos que serão mais abrangidos abaixo...')
for pos,so in enumerate(votos):
    if(so > 0):
        print(f'Sistema Operacional: {sistemas[pos]:<15} Votos: {so:<8} Porcentagem: {so/sum(votos):<10.2%}')
pos_mais_votado = votos.index(max(votos))
print(f'O sistema operacional  mais votado foi {sistemas[pos_mais_votado]} com {(max(votos))} votos, correspondendo a {max(votos) / sum(votos):.2%} dos votos')
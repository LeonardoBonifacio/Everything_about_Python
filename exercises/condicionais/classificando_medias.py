from os import system
system('cls')

nota_1 = float(input('Digite a primeira nota do(a) aluno(a): '))
nota_2 = float(input('Digite a segunda nota do(a) aluno(a): '))
media = (nota_1 + nota_2) / 2

if(media <= 4.9):
    print(f'Sua média foi de {media}')
    print(f'Média até 4.9: REPROVADO')
elif(media >= 5.0 and media <= 6.9):
    print(f'Sua média foi de {media}')
    print(f'Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print(f'Sua média foi de {media}')
    print(f'Média 7.0 ou superior: APROVADO')
    
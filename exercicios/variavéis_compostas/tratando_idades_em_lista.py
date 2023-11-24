from os import system
system("cls")

idades = []
posicoes = []
maiores = []
pos_maior = []
for idade in range(8):
    idades.append(int(input(f'Por favor digite a idade da {idade + 1}° pessoa: ')))
print(f'A)A média das idades informadas foi {(sum(idades)/8):.2f}')
for pos,idade in enumerate(idades):
    if(idade == (max(idades))):
        pos_maior.append(pos + 1)
    if(idade > 25):
        posicoes.append(pos + 1)
    if(pos == 0):
        maiores.append(idade)
    else:
        if(idade == max(maiores) or idade > max(maiores)):
            maiores.append(idade)
print(f'B)Nas posições {posicoes} temos pessoas com mais de 25 anos. ')
print(f'C)As maiores idades informadas foram: {maiores}')
print(f'D)A maior idade foi digitada na posição {pos_maior}')
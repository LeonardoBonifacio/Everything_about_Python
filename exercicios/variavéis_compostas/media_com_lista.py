from os import system
system('cls')


notas = []

for nota in range(1,5):
    notas.append(float(input(f'Digite a {nota}° nota: ')))
print(f'As quatro notas informadas foram: ',end = '')
print(*notas)
media = 0
for nota in notas:
    media += nota
media /= 4
print(f'E a média desa 4 notas é {media:.2f}')

#função sum() retorna a soma de todos os valores de uma lsita
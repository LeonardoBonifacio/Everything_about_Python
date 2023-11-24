from os import system
system('cls')
idades = []
alturas = []
for pessoa in range(1,6):
    idade = int(input(f'Digite a idade da {pessoa}° pessoa: '))
    altura = float(input(f'Digite a altura da {pessoa}° pessoa: '))
    idades.append(idade)
    alturas.append(altura)
idades = idades[::-1]
alturas = alturas[::-1]
print('As idades e alturas informadas na ordem inversa foram: ')
for idade,altura in zip(idades,alturas):
    print(idade,'anos',altura,'m')


from os import system
system('cls')

reais = []

for i in range(5):
    num = float(input('Digite números reais: '))
    reais.append(num)
print('Tome eles invertidos nos seu peitos...')
for reais in reais[::-1]:
    print(reais)
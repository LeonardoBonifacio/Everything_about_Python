from os import system
system('cls')

'''nome = str(input('Digite seu nome: ')).strip().title()

if(nome == 'Gustavo'):
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if(media >= 6.0):
    print('Sua média foi boa parabens!')
else:
    print('Sua mÉdia foi ruim! ESTUDE MAIS!')
# print('PARABENS' if media >= 6.0 else 'ESTUDE MAIS!' ) Representação da estrutura condicional simplificada
print(f'A sua média foi {media:.2f}')
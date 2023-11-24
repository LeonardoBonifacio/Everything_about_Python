from os import system
system('cls')
cont = media = 0
while(True):
    print('-=-' * 10,'DEPARTAMENTO ESTADUAL DE METEOROLOGIA','-=-' * 10)
    cont += 1
    temperaturas = float(input(f'Digite a {cont}° temperatura: '))
    if(cont == 1):
        maior = temperaturas
        menor = temperaturas
    if(temperaturas > maior):
        maior = temperaturas
    if(temperaturas < menor):
        menor = temperaturas
    media += temperaturas
    continuar = str(input('Continuar a informar temperaturas? [S]im ou [N]ão >>>')).strip().upper()[0]
    if(continuar == 'N'):
        break
    system('cls')
media /= cont

print(f'Das {cont} temperaturas informadas:\nA){maior:.2f}C° foi a maior lida\nB){menor:.2f}C° foi a menor lida\nC){media:.2f}C° foi a média de todas as temperaturas.')
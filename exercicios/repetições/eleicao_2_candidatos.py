from os import system
system('cls')

parar_de_votar = ''
primeiro = 0
segundo = 0
branco = 0
nulo = 0

print('Votando nos candidatos 1 e 2')

while(parar_de_votar != 'parar'):
    candidato = int(input('Em qual cadidato deseja votar?\n[1] - Primeiro candidato\n[2] - Segundo candidato\n[3] - Branco\n[4] - Nulo\n-->  '))
    if(candidato != 1 and candidato != 2 and candidato != 3 and candidato != 4):
        print('Você precisa escolher em quem votar , deixar seu voto em branco ou nulo.')
    elif(candidato == 1):
        primeiro = primeiro + 1
    elif(candidato == 2):
        segundo = segundo + 1
    elif(candidato == 3):
        branco = branco + 1
    elif(candidato == 4):
        nulo = nulo + 1
    parar_de_votar = input('Digite "parar" se os votos tiverem acabado ou so de enter para continuar : ').strip().casefold()
    system('cls')
print(f'O candidato número 1 teve exatos {primeiro} votos\nO candidato número 2 teve exatos {segundo} votos\nTiveram {branco} votos em branco\nTiverem {nulo} votos nulos ')

if(primeiro > segundo):
    print('Portanto o candidato número 1 ganhou as eleições.')
elif(segundo > primeiro):
    print('Portanto o candidato número 2 ganhou as eleições.')
else:
    print('Não houve ganhador das eleições no primeiro turno.')
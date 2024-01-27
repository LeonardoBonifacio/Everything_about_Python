from os import system
system('cls')

print('__________VIAGEM__________')

distancia = float(input('Digite a distancia que deseja percorrer em Km: '))

if(distancia <= 200.00):
    preco_passagem = 0.50 * distancia
else:
    preco_passagem = 0.45 * distancia
print(f'Você terá que pagar R${preco_passagem:.2f} pelos {distancia:.2f}km.')

#De forma simplificada ficaria
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
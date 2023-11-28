from os import system
system('cls')
media_altura = 0
pesa_mais_que_90 = 0
pessoas_magras_e_baixas = 0
pessoas_robustas_e_altas = 0
for pessoas in range(1,8):
    peso = float(input(f'Peso da {pessoas}° pessoa: '))
    altura = float(input(f'Altura da {pessoas}° pessoa: '))
    media_altura += altura
    if(peso > 90):
        pesa_mais_que_90 += 1
    if(peso < 50  and altura < 1.60):
        pessoas_magras_e_baixas += 1 
    if(altura > 1.90 and peso > 100):
        pessoas_robustas_e_altas += 1

media_altura /= 7
print(f'A média de altura do grupo foi de {media_altura:.2f}')
print(f'A quantidade de pessoas que pesam mais de 90kg é de {pesa_mais_que_90}')
print(f'{pessoas_magras_e_baixas} pessoas pesam menos de 50kg e tem menos de 1.60m')
print(f'{pessoas_robustas_e_altas} pessoas medem mais de 1.90m e pesam mais de 100kg')
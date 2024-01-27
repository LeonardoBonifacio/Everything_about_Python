from os import system 
system('cls')

print('----------MULTA----------')

velocidade_carro = float(input('Digite a velocidade do carro: '))

if(velocidade_carro > 80):
    print('Você foi multado por ultrapassar os 80km/h de velocidade estabelecidos.')
    multa = (velocidade_carro - 80) * 7
    print(f'A multa é de R$7,00 a cada km acima do limite de velocidade.\nPortanto, você irá pagar R${multa:.2f}')
else:
    print('Você não foi multado, pois não ultrapassou a velocidade limite de 80km/h')
    print('Tenha um bom dia! Dirija com segurança.')
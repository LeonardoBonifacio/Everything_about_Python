'''
Criar um programa que leia o consumo de veículo e informe a distância que vai percorrer com x litros de combustivel
'''

import os
os.system('cls')

#consumo = quantos km o carro faz com cada litro de gasolina
consumo = int(input('Qual o consumo do seu veículo: '))
gasolina = int(input('Quantos litros de gasolina você colocou: '))
distancia = consumo * gasolina

print(f'Você vai rodar {distancia}km com {gasolina}L de gasolina')
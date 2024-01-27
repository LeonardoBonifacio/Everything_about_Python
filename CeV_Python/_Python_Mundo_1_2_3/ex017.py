from os import system
system('cls')

from math import hypot #Função para calcular a hipotenusa de um triângulo retângulo

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

print(f'A hipotenusa desse triângulo retângulo é igual a {hypot(cateto_oposto,cateto_adjacente):.2f}')

#hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2) ou ** 1/2
#sqrt Função para calcular raiz quadrada


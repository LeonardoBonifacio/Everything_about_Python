from os import system
system('cls')

from math import sin,cos,tan,radians

angulo = int(input('Digite um ângulo qualquer: '))

rad = radians(angulo)

print(f'O seno desse angulo é {sin(rad):.2f}\nO cosseno desse ângulo é {cos(rad):.2f}\nA tangente desse ângulo é {tan(rad):.2f}.')
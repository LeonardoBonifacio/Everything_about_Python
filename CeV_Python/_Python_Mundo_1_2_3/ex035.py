from os import system
system('cls')

print('-----PODE FORMAR TRIÂNGULO?-----')

reta1 = float(input('Digite o comprimento da 1º reta: '))
reta2 = float(input('Digite o comprimento da 2º reta: '))
reta3 = float(input('Digite o comprimento da 3º reta: '))

if(reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2):
    print('Com esses segmentos de reta PODEM SER FORMADOS um triângulo.')
else:
    print('NÃO PODEMOS FORMAR um triângulo com esses segmentos de reta.')

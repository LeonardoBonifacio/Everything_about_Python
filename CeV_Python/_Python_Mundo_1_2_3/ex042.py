from os import system
system('cls')

print('-=-' * 14, 'PODE FORMAR? / QUE TRIÂNGULO' ,'-=-' * 14)

reta1 = float(input('Digite o comprimento do 1º segmento: '))
reta2 = float(input('Digite o comprimento do 2º segmento: '))
reta3 = float(input('Digite o comprimento do 3º segmento: '))

if(reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2):
    print('Com esses segmentos de reta podemos formar um triângulo.')
    if(reta1 == reta2 == reta3):
        print('Este é um triângulo equilátero , pois possui todos os lados iguais.')
    elif(reta1 == reta2 or reta1 == reta3 or reta2 == reta3):
        print('Este é um triângulo isoceles, pois possui dois lados iguais.')
    else:#reta1 != reta2 != reta3 != reta1
        print('Esté é um triângulo escaleno, pois não possui nenhum lado igual.')
else:
    print('Com esses segmento de reta não podemos formar um triângulo.')
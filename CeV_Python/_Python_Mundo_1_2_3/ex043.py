from os import system
system('cls')

print('-=-' * 14, 'CALCULANDO IMC' ,'-=-' * 14)

peso = float(input('Digite o seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / altura ** 2

if(imc < 18.5):
    print(f'Você está abaixo do peso, pois seu imc é de {imc:.1f}.')
elif(imc >= 18.5 and imc < 25):
    print(f'Você está no peso ideal, pois seu imc é de {imc:.1f}.')
elif(imc >= 25 and imc < 30):
    print(f'Você está com sobrepeso, pois seu imc é de {imc:.1f}.')
elif(imc >= 30 and imc < 40):
    print(f'Você está com Obesidade, pois seu imc é de {imc:.1f}.')
else:
    print(f'Você está com obesidade mórbida, pois seu imc é de {imc:.1f}')
from os import system 
system('cls')

print('__________CALCULANDO SEU IMC__________')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso / altura**2)

print(f'Seu índice de massa corporea é de {imc:.2f}')

if(imc <= 18.5):
    print('Imc abaixo de 18.5: Abaixo do peso')
elif(imc > 18.5 and imc <= 25):
    print('Imc entre 18.5 e 25: Peso ideal')
elif(imc > 25 and imc <= 30):
    print('Imc entre 25 e 30: Sobrepeso')
elif(imc > 30 and imc <= 40 ):
    print('Imc entre 30 e 40: Obesidade')
else:
    print('Imc acima de 40: Obesidade mórbida')
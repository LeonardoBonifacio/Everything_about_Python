from os import system
system('cls')

ingresso = 50

sexo = str(input('Digite[Mulher] ou  [Homem]: ')).strip().casefold()

idade = int(input('Digite sua idade: '))

if(sexo != 'mulher' and sexo != 'homem'):
    print('Você digitou um sexo inválido')
elif(idade <= 0):
    print('Você digitou um valor inválido para idade')
elif(sexo == 'mulher' and idade > 50):
    desconto = ingresso - (ingresso * 0.75)
    print(f'Você ganhou um desconto de 75% no valor do ingresso, valor a pagar R${desconto:.2f}')
    
elif(sexo == 'mulher' and idade > 40):
    desconto = ingresso - (ingresso * 0.2)
    print(f'Você ganhou um desconto de 20% no valor do ingresso, valor a pagar R${desconto:.2f}')

else:
    print('Que pena você não ganhou nenhum desconto.')
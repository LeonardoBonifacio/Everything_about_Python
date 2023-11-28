from os import system
system('cls')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if(num2 == 0):
    print('O segundo número não pode ser 0 , pois , iremos realizar a divisão inteira e resto da divisão do primeiro com o segundo número.')
else:
    dividendo = num1
    divisor = num2
    quociente = 0
    while(dividendo >= divisor):
        dividendo -= divisor
        quociente += 1
if(num2 != 0 ): 
    resto =( (quociente * divisor) - num1) * -1
    print(f'A divisão inteiro entre {num1} // {num2} = {quociente}')
    print(f'O resto da divisão entre {num1} % {num2} = {resto}')

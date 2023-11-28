from os import system
system('cls')
print('-=-' * 10,'VERIFICADOR DE NÚMEROS PRIMOS','-=-' * 10)
num = int(input('Digite o número que quer verifiar se é primo: '))
cont =  1
divisores = []
qtd_div = 0
if(num % 2 == 0):
    qtd_div += 1
while(cont <= num):
    if(num % cont == 0):
        qtd_div += 1
        divisores.append(cont)
    cont += 1
if(qtd_div > 2):
    print(f'O número {num} não é primo.')
    print(f'Pois ele é divisivel por {divisores}')
else:
    print(f'O número {num} é primo.')
    print(f'Pois ele so é divisivel por {divisores}')
'''
numero = int(input('Informe até que número você quer verificar se seus antecessores são primos: '))

for numeros in range(2,numero):
    qtd_div = 0  
    for divisor in range(1,numeros + 1):
        if numeros % divisor == 0:
            qtd_div += 1  
    if (qtd_div <= 2):
        print(f'O número {numeros} é primo.')
'''
from os import system
system('cls')
num1 = 0
num2 = 1
print(num1,end = '-')
print(num2,end = '-')
for sequentes in range(8): 
    proximo = num1 + num2 
    num1 = num2 
    num2 = proximo 
    print(proximo,end = '-')
print('Cabou')


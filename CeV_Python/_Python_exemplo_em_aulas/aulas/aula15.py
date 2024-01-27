from os import system
system('cls')

'''cont = 1

while(True):
    print(cont,'->',end = ' ')
    cont += 1
print('Acabou')'''
soma = 0
while(True):
    num = int(input('Digite um número:'))
    if(num == 999):
        break
    soma += num
print(f'A soma vale {soma}.')
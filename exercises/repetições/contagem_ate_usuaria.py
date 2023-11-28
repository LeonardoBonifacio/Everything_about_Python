from os import system
system('cls')

num = int(input('Digite qualquer número inteiro e positivo: '))

for i in range(1,num + 1):
    print(i,end = ' ')
print('Acabou!')
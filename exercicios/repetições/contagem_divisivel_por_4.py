from os import system
system('cls')

for num in range(30,0,-1):
    if(num % 4 == 0):
        print(f'[{num}]',end = ' ')
    else:
        print(num,end = ' ')
print('Acabou!') 
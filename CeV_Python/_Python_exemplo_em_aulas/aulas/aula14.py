from os import system
system('cls')

'''
for c in range(1,10):
    print(c)
print('Fim')
'''

'''
c = 1

while(c < 10):
    print(c)
    c += 1
'''
'''
n = 1
while(n != 0):
    n = int(input('Digite um valor: '))
print('Acabou')
'''

'''
r ='S'
while(r == 'S'):
    n = input('Digite um valor: ')
    r = str(input('Quer continuar? [S] ou [N]')).strip().upper()
print('Acabou')
'''

n = 1
par = impar = 0
while(n != 0):
    n = int(input('Digite um valor: '))
    if(n != 0):
        if(n % 2 == 0):
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares.')
from os import system
system('cls')

while(True):
    num = int(input('Quer ver a tabuada de qual valor?  '))
    print('-------------------------------------------------')
    if(num < 0):
        break
    cont = 1
    while(cont < 11):
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    print('-------------------------------------------------')
    input('[ENTER] - Para Continuar\n')
    system('cls')
print('Programa Tabuada Encerrado volte sempre.')
from os import system
system('cls') 


par = []
impar = []
print('Digite quaisquer 5 números impares e 5 números pares,DIFERENTES:')
while(True):
    if(len(par) == 5 and len(impar) == 5):
        break
    else:   
        num = int(input(('Digite --> ')))
        if(num % 2 == 0):
            if(num not in par):
                par.append(num)
        else:
            if(num not in impar):
                impar.append(num)
print(f'Números pares digitados: {par}')
print(f'Números impares digitados: {impar}')
from os import system
system('cls')
soma = 0
num = 0 
while(True):
    num = int(input('Número(s) a ser(em) somado(s) ou digite 1111  para parar:'))
    if(num == 1111):
        break
    else:
        soma += num
print(soma)
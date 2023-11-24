from os import system
system('cls')

while(True):
    while(True):
        num = int(input('Fatorial de: '))
        if(num > 0 and num  <= 16):
            break
        print('Por favor insira um valor entre 0 e 16')
    fatorial = 1
    numeros_fatorais  = ''
    for n in range(num,0,-1):
        if(n == 1):
            numeros_fatorais = numeros_fatorais + str(n) + ' = '
        else:
            numeros_fatorais = numeros_fatorais + str(n) + ' x '
        fatorial *= n
    print(numeros_fatorais,fatorial)
    continuar = str(input('Continuar? [S]im ou [N]ão\n>>> ')).strip().upper()[0]
    if(continuar == 'N'):
        break
    system('cls')
print('Programa fatorial finalizado com sucesso.')


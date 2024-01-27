def leiaDinheiro(msg):
    liberado = False
    while(liberado == False):
        valor = input(msg).replace(',','.').strip()
        if(valor.isalpha() or valor == ''):
            print(f'ERRO \"{valor}\" não é um preço válido.')
        else:
            liberado = True
    return float(valor)

def leiaInt(msg):
    ok = False
    valor = 0
    while(True):
        n = str(input(msg))
        if(n.isnumeric() == True):
            valor = n
            ok = True
        else:
            print('\033[0;31mERRO ! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if(ok == True):
            break
    return valor
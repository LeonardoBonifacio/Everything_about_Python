from os import system
system('cls')

while(True):
    print('===' * 10)
    print('          BANCO DO LEO          ')
    print('===' * 10)
    valor = int(input('Que valor você quer sacar? R$'))
    cinquenta = valor // 50
    valor -= cinquenta * 50
    vinte = valor // 20
    valor -= vinte * 20
    dez = valor // 10
    valor -= dez * 10
    um = valor // 1
    valor -= um * 1
    if(valor == 0):
        break
print('Você receberá...')
if(cinquenta > 0):
    print(f'{cinquenta} cêdula(s) de R$50')
if(vinte > 0):
    print(f'{vinte} cêdula(s) de R$20')
if(dez > 0):
    print(f'{dez} cêdula(s) de R$10')
if(um > 0):
    print(f'{um} cêdula(s) de R$1')
print('===' * 10)
print('Volte sempre ao BANCO DO LEO! Tenha um bom dia!')

"""
Código do Guanabara

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 0
totced = 0
while(True):
    if(total >= ced):
        total -= ced
        totced += 1
    else:
        if(totced > 0):
            print(f'Total de {totced} céduulas de R${ced}')
        if(ced == 50):
            ced = 20
        elif(ced == 20):
            ced = 10
        elif(ced == 10):
            ced = 1
        totced = 0
        if(total == 0):
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!)
"""
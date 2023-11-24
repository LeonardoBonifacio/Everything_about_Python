from os import system
system('cls')
deseja = 'jabuticaba'
while(deseja != 'N'):
    print('CAIXA DA CAIXA')
    valor = float(input('Digite o valor do saque\n>>>R$  '))
    duzentos = valor // 200
    valor -= duzentos * 200
    cem = valor // 100
    valor -= cem * 100
    cinquenta = valor // 50
    valor -= cinquenta * 50
    vinte = valor // 20
    valor -= vinte * 20
    dez = valor// 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    dois = valor // 2
    valor -= dois * 2
    um = valor // 1
    valor -= um * 1
    cinquenta_centavos = valor // 0.50
    valor -= cinquenta_centavos * 0.50
    dez_centavos = valor // 0.10
    valor -= dez_centavos * 0.10
    cinco_centavos = valor // 0.05
    valor -= cinco_centavos * 0.05
    dois_centavos = valor // 0.02
    valor -= dois_centavos * 0.02
    um_centavo = valor // 0.01
    valor -= um_centavo * 0.01     
    if(duzentos > 0):
        print(f'Você receberá {duzentos:.0f} notas de R$200')
    if(cem > 0):
        print(f'Você receberá {cem:.0f} notas de R$100')
    if(cinquenta > 0):
        print(f'Você receberá {cinquenta:.0f} notas de R$50')
    if(vinte > 0):
        print(f'Você receberá {vinte:.0f} notas de R$20')
    if(dez > 0):
        print(f'Você receberá {dez:.0f} notas de R$10 ')
    if(cinco > 0):
        print(f'Você reberá {cinco:.0f} notas de R$5')
    if(dois > 0):
        print(f'Você receberá {dois:.0f} notas de R$2')
    if(um > 0):
        print(f'Você receberá {um:.0f} notas de R$1')
    if(cinquenta_centavos > 0):
        print(f'Você receberá {cinquenta_centavos:.0f} moedas de R$0.50')
    if(dez_centavos >0):
        print(f'Você receberá {dez_centavos:.0f} moedas de R$0.10')
    if(cinco_centavos > 0):
        print(f'Você receberá {cinco_centavos:.0f} moedas de R$0.05')
    if(dois_centavos > 0):
        print(f'Voce receberá {dois_centavos:.0f} moedas de R$0.02')
    if(um_centavo > 0):
        print(f'Você receberá {um_centavo:.0f} moedas de R$0.01')
    deseja = str(input('Deseja digitar um novo valor [S]im ou [N]ão >>')).strip().upper()[0]
    system('cls')
print('Caixa da caixa informa, tome no seu cu...')
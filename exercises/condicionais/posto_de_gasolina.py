'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
from os import system
system('cls')

print('-=--=- POSTO IPIRANGA -=--=-')

alcool_ou_gasolina = str(input('Digite [A] para Álcool\nDigite [G] para Gasolina\n>>> ')).strip().upper()
litros = int(input('Digite quantos litros vai abastecer: '))
if(alcool_ou_gasolina != 'A' and alcool_ou_gasolina != 'G'):
    print('Sabe escolher certo não? é A ou G')
else:
    if(litros < 0):
        print('Então você não vai abastecer e so veio bater papo fidades')
    else:
        if(alcool_ou_gasolina == 'A'):
            if(litros <= 20):
                preco = (litros * 1.90) - ((litros * 1.90) * 0.03)
            elif(litros > 20):
                preco = (litros * 1.90) - ((litros * 1.90) * 0.05)
        elif(alcool_ou_gasolina == 'G'):
            if(litros <= 20):
                preco = (litros * 2.50) - ((litros * 2.50) * 0.04)
            elif(litros > 20):
                preco = (litros * 2.50) - ((litros * 2.50) * 0.06)
            
print('Parabens ein se conseguiu abastecer')
print(f'Agora passe pra ca R${preco:.2f}')
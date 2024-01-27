us_dinheiro = float(input('Quanto dinheiro você têm na carteira: R$'))
conver_dolar = us_dinheiro / 5.05
conver_euro = us_dinheiro / 5.51

print(f'Com os seus R${us_dinheiro:.2f} você poderia ter US{conver_dolar:.2f} e Euros{conver_euro:.2f}.')
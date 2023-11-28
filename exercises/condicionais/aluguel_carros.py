from os import system
system('cls')

print('__________ALUGUEL DE CARROS__________')
tipo_carro = int(input('[1] - Carro Popular\n[2] - Carro Luxo\n-> '))
qtd_dias = int(input('Por quantos dias deseja alugar o carro: '))
km_percorridos = float(input('Quantos serão os km percorridos: '))

if(tipo_carro == 1):
    diaria = 90 *qtd_dias
    if(km_percorridos <= 100.00):
        pagamento_km = 0.20 * km_percorridos
        valor_total = pagamento_km + diaria
        print(f'Você escolheu um carro popular,vai aluga-lo por {qtd_dias} dias e vai percorrer {km_percorridos:.2f}km')
        print(f'Valor pago pela diária R${diaria:.2f}\nValor pago pelos km rodados R${pagamento_km:.2f}\nValor total a ser pago R${valor_total:.2f}.')
    else:
        pagamento_km = 0.10 * km_percorridos
        valor_total = diaria + pagamento_km
        print(f'Você escolheu um carro popular, vai aluga-lo por {qtd_dias} dias e vai percorrer {km_percorridos:.2f}km')
        print(f'Valor pago pela diária R${diaria:.2f}\nValor pago pelos km rodados R${pagamento_km:.2f}\nValor total a ser pago R${valor_total:.2f}.')
elif(tipo_carro == 2):
    diaria = 150 * qtd_dias
    if(km_percorridos <= 200.00):
        pagamento_km = 0.30 * km_percorridos
        valor_total = pagamento_km + diaria
        print(f'Você escolheu um carro de luxo,vai aluga-lo por {qtd_dias} dias e vai percorrer {km_percorridos:.2f}km')
        print(f'Valor pago pela diária R${diaria:.2f}\nValor pago pelos km rodados R${pagamento_km:.2f}\nValor total a ser pago R${valor_total:.2f}')
    else:
        pagamento_km = 0.25 * km_percorridos
        valor_total = diaria + pagamento_km
        print(f'Você escolheu um carro de luxo,vai aluga-lo por {qtd_dias} dias e vai percorrer {km_percorridos:.2f}km')
        print(f'Valor pago pela diária R${diaria:.2f}\nValor pago pelos km rodados R${pagamento_km:.2f}\nValor total a ser pago R${valor_total:.2f}')
else:
    print('Você não escolheu o tipo de carro.')